from django.shortcuts import render,redirect
from Task import models
from Task.models import TaskModel  # Import TaskModel from Task app
from Category.models import CategoryModel  # Import CategoryModel from Category app
from Task import forms 
# Create your views here.
def task(request):
    if request.method =='POST':
        task_form =forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
    
    else:
         task_form =forms.TaskForm()
    return render(request,'add_task.html',{'form':task_form})


def edit(request,id):
    
    post =models.TaskModel.objects.get(pk=id)
    task_form =forms.TaskForm(instance= post)
    
    if request.method =='POST':
        task_form =forms.TaskForm(request.POST,instance=post)
        if task_form.is_valid():
          task_form.save()
    
   
    return render(request,"add_post.html",{'form':task_form} )

def delete(request,id):
     post =models.TaskModel.objects.get(pk=id)
     post.delete()
     return redirect("view_page")
   
     
    