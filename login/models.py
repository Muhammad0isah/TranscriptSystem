from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
