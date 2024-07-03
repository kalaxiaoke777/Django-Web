from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer


class UserRegisterAPIView(viewsets.ViewSet):
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            CustomUser.objects.create_user(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
                telephone_number=serializer.validated_data.get("telephone_number", ""),
                chooes=serializer.validated_data.get("chooes", ""),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):

        return JsonResponse(
            {
                "message": "登录成功",
                "code": 200,
                "success": True,
            }
        )
