from django.conf import settings
from django.db import models


# DEFAULT_TODOLIST_ID = 1
# class TodoList(models.Model):
#     User = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name="todolist",  on_delete=models.CASCADE, default=None, db_column="user_id")
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     # order = models.IntegerField(max_length=11)

#     class Meta:
#         ordering = ['title']


class Todo(models.Model):
    # user = models.ForeignKey(
    # settings.AUTH_USER_MODEL, related_name="todolist",  on_delete=models.CASCADE, default=None, db_column="user_id")
    # todolist = models.ForeignKey(
    #     'TodoList', related_name='todos', on_delete=models.CASCADE, default=DEFAULT_TODOLIST_ID)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # order = models.IntegerField(max_length=11)
    remind_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
