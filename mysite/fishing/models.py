from django.db import models
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    english = models.CharField(max_length=30)
    chinese = models.CharField(max_length=30)
