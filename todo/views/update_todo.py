from django.shortcuts import render, redirect, get_object_or_404
from todo.models import TodoModel

def update_todo(request, id):
    todo = get_object_or_404(TodoModel, id=id)
    todo.is_completed = not todo.is_completed

    todo.save()
    return redirect('/')
        
