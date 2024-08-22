from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password", "confirm_password"]

        extra_kwargs = {
            "password" : {
                "write_only" : True,
            }
        }

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise ValidationError("Password and Confirm Password Does Not Matched!")
        
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email Address Exists!")
        
        account = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email)

        account.set_password(password)
        account.save()
        return account
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)