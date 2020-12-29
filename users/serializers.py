from django.contrib.auth.models import User, Group
from rest_framework import serializers

from todos.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
