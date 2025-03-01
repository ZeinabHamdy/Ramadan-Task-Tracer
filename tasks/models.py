from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
    )
    goal = models.IntegerField(
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    status = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    current_achieved = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return self.title