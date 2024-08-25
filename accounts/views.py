from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.serializers import CustomUserSerializer, RegistrationSerializer, LoginSerializer, ProfileSerializer



class CustomUserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = [IsAdminUser]


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class RegistrationViews(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response({"message" : "Registration Successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginViewset(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                token , _ = Token.objects.get_or_create(user=user)
                # print(token)
                # print(_)

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
    

   


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            print(token)
            token.delete()
            return Response({
                "message": "Logout Successfully!",
            }, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token Does Not Exist!"}, status=status.HTTP_400_BAD_REQUEST)


