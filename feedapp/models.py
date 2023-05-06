from django.contrib.auth.models import User
from django.db import models


class Feed(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feed")

    image = models.ImageField(upload_to="feed/", null=True)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
