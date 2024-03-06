from rest_framework.response import Response
from rest_framework.views import APIView
from django_otp.oath import TOTP
from hashlib import sha1 
from .models import *
from .serializers import *
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from rest_framework.generics import get_object_or_404


class OTPGenerationView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        
        # Check if OTP already exists for the given phone number
        existing_otp = OTP.objects.filter(phone_number=phone_number).exists()
        if existing_otp:
            return Response({"phone_number": ["otp with this phone number already exists."]}, status=400)
        
        # Generate and save OTP
        user_otp = OTP.objects.create(phone_number=phone_number)
        key = bytes(str(user_otp.pk), 'utf-8')  
        totp = TOTP(key=key) 
        otp = totp.token()
        
        # Save OTP to user's otp field
        user_otp.otp = otp
        user_otp.save()
        
        return Response({'otp': otp})

    def delete_expired_otps(self):
        ten_minutes_ago = timezone.now() - timedelta(minutes=10)
        OTP.objects.filter(created_at__lt=ten_minutes_ago).delete()

class LoginView(APIView):
    def post(self, request):
        serializer = OTPLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_otp = serializer.validated_data['otp']
        phone_number_id = request.data.get('phone_number_id') 
        
        try:
            # Retrieve the OTP from the database based on the phone number
            user_otp = OTP.objects.get(pk=phone_number_id)
        except OTP.DoesNotExist:
            return Response({"detail": "User with this phone number ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the input OTP matches the saved OTP
        if input_otp != user_otp.otp:
            return Response({"detail": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Successful login, perform additional actions here if needed
        return Response({"detail": "Login successful."})
    


class PanView(APIView):
    def post(self, request):
        serializer = PANSerializer(data=request.data)
        if serializer.is_valid():
            phone_number_id = request.data.get('phone_number')  
            
            # Fetch the corresponding OTP instance or return 404 if it doesn't exist
            phone_number_instance = get_object_or_404(OTP, id=phone_number_id) 
            
            serializer.save(phone_number=phone_number_instance)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

