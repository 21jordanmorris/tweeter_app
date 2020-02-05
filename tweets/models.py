from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    body = models.CharField(max_length=255)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body