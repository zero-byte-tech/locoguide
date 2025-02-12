from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,OTP
from .serializers import UserRegistrationSerializer,OTPSerializer,PasswordSetSerializer,LoginSerializer
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

class RegisterView(APIView):
    def post(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            
            otp=random.randint(100000,999999)
            OTP.objects.create(user=user,otp=otp)
            
            send_mail(
                'Verify your email',
                f'Your otp is {otp}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            return Response({'message':"OTP sent to email"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class VerifyOTPView(APIView):
    def post(self,request):
        serializer=OTPSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            otp=serializer.validated_data['otp']
            
            try:
                user=User.objects.get(email=email)
                otp_obj=OTP.objects.filter(user=user).last()
                if otp_obj.otp==otp:
                    user.is_verified=True
                    user.save()
                    return Response({'message':"OTP verified succesfully"})
                return Response({'message':"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'message':"User not found"},status=404)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SetPasswordView(APIView):
    def post(self,request):
        serializer=PasswordSetSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            
            try:
                user=User.objects.get(email=email)
                user.set_password(password)
                user.save()
                return Response({'message':"Password set successfully"})
            except User.DoesNotExist:
                return Response({'message':"User not found"},status=404)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(email=serializer.validated_data['email'],password=serializer.validated_data['password'])
            tokens=get_tokens_for_user(user)
            return Response(tokens)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
                
                