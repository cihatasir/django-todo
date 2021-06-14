from django.urls import path, include
from todo.views import base

urlpatterns = [
    path('', base, name='base'),
]
