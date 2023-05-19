from django.contrib.auth.models import User
from django.db import models

from feedapp.models import Feed


class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True, related_name="comment")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comment")

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
