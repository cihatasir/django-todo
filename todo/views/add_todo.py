from django.shortcuts import render, redirect
from todo.models import TodoModel

def add_todo(request):
    if request.method == "GET":
        return redirect("/")
   
    else:
        title = request.POST.get('todoTitle')
        new_todo = TodoModel(title=title, is_completed=False)
        new_todo.save()
        return redirect("/")
        
