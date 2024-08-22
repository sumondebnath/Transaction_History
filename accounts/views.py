from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, RegistrationSerializer, LoginSerializer



class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RegistrationViews(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            # token = default_token_generator.make_token(user)
            # uid = urlsafe_base64_encode(force_bytes(user.pk))
            return Response({"message" : "Registration Successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginViewset(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = self.request.data)
        token = default_token_generator.make_token(self.request.user)
        uid = urlsafe_base64_encode(force_bytes(self.request.user.pk))

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)

            if user:
                token , _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)

                login(request, user)
                return Response({
                    "token" : token.key, 
                    "user_id" : user.id}, 
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "error" : "Invalid Credential!",
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)