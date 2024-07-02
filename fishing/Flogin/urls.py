from django.urls import path

from . import views

urlpatterns = [
    # path("login", views.UserRegisterAPIView.login(), name="login"),
    path(
        "register",
        views.UserRegisterAPIView.as_view({"get": "register"}),
        name="register",
    ),
    path(
        "login",
        views.UserRegisterAPIView.as_view({"get": "login"}),
        name="login",
    ),
]
