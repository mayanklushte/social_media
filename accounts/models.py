from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Mobile_No = models.CharField(max_length=10)
    bio = models.CharField(max_length=120)
    profile_picture = models.ImageField(upload_to='profile_pic')
    link = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
