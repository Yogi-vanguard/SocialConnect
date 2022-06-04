from asyncore import read
import profile
import re
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.utils import searchHelper
from projects.variables.constant import Constants
from .models import Project,Review,Tag
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchHelper,paginatorHelper
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage



# Create your views here.
def projects(request):
    projects,search_query = searchHelper(request)
    
    projects,paginator,custom_range = paginatorHelper(request,projects,result=3)
    context = {"projects":projects,"search_query":search_query,"paginator":paginator,"custom_range":custom_range}
    return render(request, 'projects/projects.html',context)


def project(request, pk):
    item = Project.objects.get(id=pk)
    tag = item.tags.all()
    context = {"project":item,"tags":tag}
    return render(request, 'projects/single-project.html',context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method=="POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request,"Project Added Successfully!")
            return redirect('account')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url='login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request,"Project Updated Successfully!")
            return redirect('account')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method=="POST":
        project.delete()
        messages.success(request,"Project Deleted Successfully!")
        return redirect('projects')
    context = {'object':project}
    return render(request,'delete_template.html',context)    