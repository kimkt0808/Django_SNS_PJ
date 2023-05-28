from django.contrib.auth.models import User
from django.db import models

from feedapp.models import Feed


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "feed"], name="unique_like")
        ]
