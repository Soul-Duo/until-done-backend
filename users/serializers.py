from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from todos.models import Todo


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all(), default=[])

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'todos', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(
                validated_data['password'])  # encrypt password
        )
        user.save()
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = make_password(
            validated_data.get('password', instance.password))
        instance.save()
        return instance
