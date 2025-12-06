from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Tweet(models.Model):
    text = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="tweets/", blank=True, null=True)

    def __str__(self):
        return self.user.username + ": " + self.text[:50]
