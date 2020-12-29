from django.conf import settings
from django.db import models


class Todo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # order = models.IntegerField(max_length=11)
    remind_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
