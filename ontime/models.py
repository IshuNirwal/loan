from django.db import models
from django.utils import timezone

class OTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.phone_number
    
class PAN(models.Model):
    number = models.CharField(max_length=10, unique=True)
    phone_number = models.ForeignKey(OTP, on_delete=models.CASCADE, related_name='pans')

    def __str__(self):
        return self.number
    
class ADHAR(models.Model):
    adhar_number = models.IntegerField( unique=True)
    phone_number = models.ForeignKey(OTP, on_delete=models.CASCADE, related_name='adhar')

    def __str__(self):
        return self.adhar_number
    
class BANK(models.Model):
    name = models.CharField(max_length=100)
    account_number=models.IntegerField(unique=True)
    ifsc=models.CharField(max_length=20)
    phone_number = models.ForeignKey(OTP, on_delete=models.CASCADE, related_name='bank')

    def __str__(self):
        return self.name
    
class DOCUMENT(models.Model):
    salary_slip = models.FileField(upload_to='documents/')
    bank_statement = models.FileField(upload_to='documents/')
    phone_number=models.ForeignKey(OTP,on_delete=models.CASCADE, related_name='doc')

    def __str__(self):
        return self.salary_slip
    
