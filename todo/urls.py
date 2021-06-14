from django.urls import path
from todo.views import add_todo, base, update_todo, delete_todo

urlpatterns = [
    path('', base),
    path('add-todo', add_todo, name='add-todo'),
    path('update_todo/<int:id>', update_todo, name='update-todo'),
    path('delete_todo/<int:id>', delete_todo, name='delete-todo'),

]

