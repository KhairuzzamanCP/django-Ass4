from django.shortcuts import render, redirect
from .models import TaskModel
from .import forms
# Create your views here.
def showtask(request):
    data = TaskModel.objects.all()
    return render(request, 'task.html',{'data':data})
def delete(request,id):
    data =TaskModel.objects.get(pk=id).delete()
    return redirect('show_task')

def add(request):
    if request.method == 'POST':
        post = forms.TaskForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('show_task')
    else:
        post =forms.TaskForm()
    return render(request,'add.html',{'form':post})
    
    
def edit(request,id):
    edit_item =  TaskModel.objects.get(pk= id)
    form = forms.TaskForm(instance=edit_item)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance= edit_item)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render(request,'add.html',{'form':form})

    