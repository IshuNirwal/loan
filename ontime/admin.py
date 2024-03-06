from django.contrib import admin
from .models import *

class OTPAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','otp',)  

admin.site.register(OTP, OTPAdmin)

class PANAdmin(admin.ModelAdmin):
    list_display = ('id','number','phone_number')  

admin.site.register(PAN, PANAdmin)
