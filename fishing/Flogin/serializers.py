from rest_framework import serializers


class UserRegistrationForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    telephone_number = serializers.CharField()
