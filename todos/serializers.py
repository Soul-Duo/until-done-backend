from rest_framework import serializers

from .models import Todo


# class TodoListSerializer(serializers.ModelSerializer):
#     user_id = serializers.RelatedField(source='user')

#     class Meta:
#         model = TodoList
#         fields = ['user_id', 'title', 'description']


class TodoSerializer(serializers.ModelSerializer):
    # user_id = serializers.RelatedField(source='user', read_only=True)
    # todolist_id = serializers.RelatedField(source='todolist')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'remind_at', 'created_at', 'completed']
