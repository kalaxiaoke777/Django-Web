from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer


class UserRegisterAPIView(viewsets.ViewSet):

    def register(self, request):
        serializer = UserSerializer(data=request.data)
        # Validate the data
        # 这样做拦截不知道对不对
        serializered = serializer.is_valid()
        validated_data = serializer.validate_username_email(
            username=serializer.data["username"], email=serializer.data["email"]
        )
        if validated_data:
            # 这里应该有些简单验证的逻辑
            CustomUser.objects.create_user(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
                telephone_number=serializer.validated_data.get("telephone_number", ""),
                chooes=serializer.validated_data.get("chooes", ""),
            )
            return JsonResponse(
                {
                    "message": "注册失败,用户名重复",
                    "code": 400,
                    "success": False,
                    "data": [],
                }
            )
        return JsonResponse(
            {"message": "注册成功", "code": 200, "success": True, "data": []}
        )

    def login(self, request):
        # DRF处理token,其实就是验证用户名密码,然后生成token前端将token持久化
        # 从请求中获取用户名和密码
        username = request.query_params["username"]
        password = request.query_params["password"]

        # 使用 Django 的 authenticate 方法验证用户名和密码
        user = authenticate(username=username, password=password)

        # 如果验证成功
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            # 返回成功登录的响应
            return JsonResponse(
                {
                    "message": "登录成功",
                    "code": status.HTTP_200_OK,
                    "success": True,
                    "token": token.key,  # 返回生成的 token 给前端
                }
            )
        else:
            # 如果验证失败，返回错误信息
            return JsonResponse(
                {
                    "message": "用户名或密码错误",
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "success": False,
                }
            )
