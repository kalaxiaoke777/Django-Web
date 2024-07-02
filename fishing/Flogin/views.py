from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import UserManager

from .serializers import UserRegistrationForm


class UserRegisterAPIView(viewsets.ViewSet):
    def register(self, request):
        serializer = UserRegistrationForm(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            email = serializer.validated_data["email"]
            telephone_number = serializer.validated_data["telephone_number"]

            # 检查用户名是否已存在
            if User.objects.filter(username=username).exists():
                pass
            # 创建用户
            user = UserManager.create_user(
                username=username,
                password=password,
                email=email,
                telephone_number=telephone_number,
            )

            # 可以根据需要进行其他操作，比如发送确认邮件等

            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
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
