from django.contrib.auth.models import User
from django.db import models


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")
    follow_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_user")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "follow_user"], name="unique_follow")
        ]
