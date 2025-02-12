from django.urls import path
from .views import RegisterView,VerifyOTPView,SetPasswordView,LoginView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('verify-otp/',VerifyOTPView.as_view(),name='verify-otp'),
    path('set-password/',SetPasswordView.as_view(),name='set-password'),
    path('login/',LoginView.as_view(),name='login'),
]
