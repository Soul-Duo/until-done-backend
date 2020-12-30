from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserCreate

urlpatterns = format_suffix_patterns([
    path('', UserCreate.as_view(), name='user_create'),
])
