from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20)
    # password
    # description
    # category

    class Meta:
        ordering = ["-pk"]
