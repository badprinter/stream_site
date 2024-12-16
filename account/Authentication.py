from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from stream_web_site import settings


class TokenCookieAuthentication(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = self.authenticate(request)
        if user is not None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        response = Response({"detail": "Login successful"})
        response.set_cookie(
            key='auth_token',
            value=token.key,
            httponly=True,
            secure=True if settings.DEBUG else False, # Secure только в продакшн среде
            samesite='Strict',
        )
        return response


    def authenticate(self, request):
        """
        Метод аутентификации пользователя через username и password
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        return user