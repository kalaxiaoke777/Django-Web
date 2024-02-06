from django.urls import path

from . import views

urlpatterns = [
    path("addPoint", views.addPoint, name="addPoint"),
    path("deletePoint", views.deletePoint, name="deletePoint"),
    path("updataPoint", views.updataPoint, name="updataPoint"),
    path("fieldName", views.fieldName, name="fieldName"),
]
