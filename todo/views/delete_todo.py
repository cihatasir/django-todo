from django.shortcuts import render, redirect, get_object_or_404
from todo.models import TodoModel

def delete_todo(request, id):
    todo = get_object_or_404(TodoModel, id=id)
    todo.delete()

    return redirect('/')
        
