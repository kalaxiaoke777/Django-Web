from rest_framework import serializers
from .models import CustomUser
from typing import Union


class UserSerializer(serializers.ModelSerializer):

    def validate_username_email(self, username: str, email: str) -> Union[bool, list]:
        # Check if username or email already exist
        if (
            CustomUser.objects.filter(username=username).exists()
            or CustomUser.objects.filter(email=email).exists()
        ):
            return False
        else:
            return [True, username, email]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = CustomUser
        fields = ["username", "email", "telephone_number", "chooes", "password"]
        extra_kwargs = {"password": {"write_only": True}}
