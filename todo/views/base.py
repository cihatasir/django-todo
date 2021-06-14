from django.shortcuts import render, redirect
from todo.models import TodoModel

def base(request):
    todos = TodoModel.objects.all()

    return render(request, "base.html", {
        'todos':todos
    })
    
