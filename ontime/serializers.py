from rest_framework import serializers
from .models import *
import re

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('phone_number',) 


class OTPLoginSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)


class PANSerializer(serializers.ModelSerializer):
    def validate_number(self, value):
        # PAN card number format regex pattern
        pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

        if not re.match(pan_pattern, value):
            raise serializers.ValidationError("Enter a valid PAN card number.")
        return value

    class Meta:
        model = PAN
        fields = ('number',)

class ADHARSerializer(serializers.ModelSerializer):
    class Meta:
        model=ADHAR
        fields=('adhar_number',)

class BANKSerializer(serializers.ModelSerializer):
    class Meta:
        model=BANK
        fields=('name','account_number','ifsc')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOCUMENT
        fields = ['salary_slip', 'bank_statement']

