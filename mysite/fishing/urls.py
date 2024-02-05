from django.urls import path

from . import views

urlpatterns = [
    path("addPoint", views.addPoint, name="addPoint"),
]
