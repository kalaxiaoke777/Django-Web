import login.views
from django.urls import path, include

urlpatterns = [
    path("login/", login.views.login),
    path("register/", login.views.register),
]
