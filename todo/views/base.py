from django.shortcuts import render, redirect
from todo.models import TodoModel

def base(request):
    return render(request, "base.html", {})
    
