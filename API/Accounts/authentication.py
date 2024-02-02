from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class LoginAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            if request.user.is_authenticated:
                return request.user, None
        except Exception:
            raise exceptions.AuthenticationFailed('No user logged in')
