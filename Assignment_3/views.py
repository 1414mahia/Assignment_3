from django.shortcuts import render,redirect
from Task.models import TaskModel
def home(request):
    data =TaskModel.objects.all()
    return render(request,'view.html' ,{'data':data}) # html page er nam