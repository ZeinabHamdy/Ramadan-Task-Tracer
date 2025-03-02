from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator


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
        validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    current_achieved = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    progress = models.IntegerField(
        default = 0,
    )

    # i need to calculate progress 


    def save(self, *args, **kwargs):
        self.progress = (min(self.goal, self.current_achieved) / self.goal) * 100
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title