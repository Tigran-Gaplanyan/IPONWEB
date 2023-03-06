import random
import string

#
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.core.mail import send_mail
from django.conf import settings

#
from ..verification import Verification

#
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


#
from .serializers import LoginSerializer
from .serializers import RegistrationSerializer


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user.is_active:
            login(request, user)
            return HttpResponse(status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationAPIView(APIView):
    def send_verification_email(user_email):
        verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        email_body = render_to_string('verification_email_template.html', {'verification_code': verification_code})

        send_mail(
            'Verify Your Account',
            email_body,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        return verification_code

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_user_model().objects.get(username=serializer.data['username'])
            verification = Verification.objects.create(user=serializer.data[user])
            verification.save()
            self.send_verification_email()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return HttpResponse(status=status.HTTP_200_OK)


class VerifyUserAPIView(APIView):
    def post(self, request):
        verification_code = request.data.get('verification_code')
        user_email = request.data.get('user_email')

        try:
            user_profile = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return HttpResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if verification_code == user_profile.verification_code:
            user_profile.is_verified = True
            user_profile.save()
            return HttpResponse({'message': 'User verified successfully.'}, status=status.HTTP_200_OK)
        else:
            return HttpResponse({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)


