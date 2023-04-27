from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    SEX_CHOICES = (
        ("F", "Female"),
        ("M", "Male")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    image = models.ImageField(upload_to="profile/", null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    introduction = models.TextField(max_length=200, null=True)
    email = models.EmailField(max_length=128, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
