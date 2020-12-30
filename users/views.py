from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics

from .serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()
