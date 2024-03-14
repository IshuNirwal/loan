from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('otp/', OTPGenerationView.as_view(), name='otp_generation'),
    path('pan/',PanView.as_view(),name='pan'),
    path('adhar/',ADHARView.as_view(),name='adhar'),
    path('bank/',BANKView.as_view(),name='bank'),
    path('doc/',DocumentUploadView.as_view(),name='doc'),
    path('contact/',ContactEnquiryView.as_view(),name='contact'),
]
