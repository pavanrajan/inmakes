from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todoupdate
import urllib
import urllib.request
# Create your views here.
def homepage(request):
    task1 = Todo.objects.all()
    if request.method=='POST':
        task=request.POST['task']
        priority=request.POST['priority']
        date=request.POST['date']
        todo=Todo(task=task,priority=priority,date=date)
        todo.save()
    print('task created succesfully')
    return render(request,'homepage.html',{'task1':task1})
def delete(request,taskid):
    task=Todo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    todo=Todo.objects.get(id=id)
    todo1=Todoupdate(request.POST or None, instance=todo)
    if todo1.is_valid():
        todo1.save()
        return redirect('/')
    return render(request,'update.html',{'todo':todo,'todo1':todo1})





