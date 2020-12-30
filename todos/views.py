import json

from django.core import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Todo
from .serializers import TodoSerializer


JSONSerializer = serializers.get_serializer('json')


class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `create`, `retrieve`,
    `update`, and `destroy` actions.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     owner = self.request.user
    #     return Todo.objects.filter(owner=owner)

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body)
        title = body['title']
        description = body['description']
        owner = User.objects.get(pk=request.user.id)
        todo = Todo(
            title=title, description=description, owner=owner)
        todo.save()

        # Totally a workaround
        json_serializer = JSONSerializer()
        data = json_serializer.serialize(Todo.objects.filter(pk=todo.id))
        actual_data = json.dumps(json.loads(data)[0]['fields'])
        return HttpResponse(content=actual_data, content_type='application/json')

    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs["pk"])
        if not request.user.id == todo.owner:
            raise PermissionDenied("You can not delete this todo.")
        return super().destroy(request, *args, **kwargs)
