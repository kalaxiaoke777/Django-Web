from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "telephone_number", "chooes", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
