from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from .models import ToDo
from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import ToDo


# Create your views here.

def list_todo_items(request):
    # return HttpResponse('Hello')
    context = {'todo_list':ToDo.objects.all()}
    return render(request, 'todo_list.html', context)


def insert_todo_item(request: HttpRequest):
    todo = ToDo(content=request.POST['content'])
    todo.save()
    return redirect('/')
def delete_todo_item(request, todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/')
