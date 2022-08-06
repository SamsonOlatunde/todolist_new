from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    if request.method =="POST":
        new_title = Todo(
            title = request.POST['title']
        )
        new_title.save()
        return redirect('/')
    
    return render(request, 'index.html', {'todos':todo})


def delete(request, pk):
    todo_delete = Todo.objects.get(id=pk)
    todo_delete.delete()
    return redirect('/')

