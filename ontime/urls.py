from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('otp/', OTPGenerationView.as_view(), name='otp_generation'),
    path('pan/',PanView.as_view(),name='pan'),
]
