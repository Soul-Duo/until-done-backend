from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(
        User, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # order = models.IntegerField(max_length=11)
    remind_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
