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

    
class ADHAR(models.Model):
    adhar_number = models.IntegerField( unique=True)
    phone_number = models.ForeignKey(OTP, on_delete=models.CASCADE, related_name='adhar')


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


class ContactEnquiry(models.Model):
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField(unique=True)
    address=models.CharField(max_length=500)
    message=models.TextField()


    def __str__(self):
        return f"{self.name1}"
    
class About(models.Model):
    image=models.ImageField(upload_to='documents/')
    text=models.TextField()

   
    
