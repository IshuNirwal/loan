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