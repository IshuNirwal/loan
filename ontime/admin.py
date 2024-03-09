from django.contrib import admin
from .models import *

class OTPAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','otp',)  

admin.site.register(OTP, OTPAdmin)

class PANAdmin(admin.ModelAdmin):
    list_display = ('id','number','phone_number')  

admin.site.register(PAN, PANAdmin)

class ADHARAdmin(admin.ModelAdmin):
    list_display = ('id','adhar_number','phone_number')  

admin.site.register(ADHAR, ADHARAdmin)

class BANKAdmin(admin.ModelAdmin):
    list_display = ('id','name','account_number','ifsc','phone_number')  

admin.site.register(BANK, BANKAdmin)


class DOCAdmin(admin.ModelAdmin):
    list_display = ('id','salary_slip','bank_statement','phone_number')  

admin.site.register(DOCUMENT, DOCAdmin)
