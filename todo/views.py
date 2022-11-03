from django.http import request
from django.shortcuts import render, redirect

from todo.forms import todoform
from todo.models import todo


# Create your views here.

def home(request):

    return render(request, 'todo.html')

def add(request):
    form=todoform()
    todos=todo.objects.all()
    if request.method=='POST':
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add.html',{'form':form,'todos':todos})




def viewf(request):
    data=todo.objects.all()
    return render(request, 'view.html',{'data':data})

def update(request,id):
    todo1=todo.objects.get(id=id)
    form=todoform(instance=todo1)
    if request.method=='POST':
        form=todoform(request.POST,instance=todo1)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update.html',{'form':form})


def delete(request,id):

        todo.objects.get(id=id).delete()
        return redirect('viewf')







