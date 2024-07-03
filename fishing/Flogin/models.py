from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        username,
        email,
        password=None,
        telephone_number="",
        chooes="",
        **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            telephone_number=telephone_number,
            chooes=chooes,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    telephone_number = models.CharField(max_length=30, blank=True)
    user_id = models.AutoField(primary_key=True)
    chooes = models.CharField(max_length=30)
    objects = CustomUserManager()

    def __str__(self):
        return self.username
