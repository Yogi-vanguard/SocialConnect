from django.shortcuts import render
from django.http import HttpResponse
from projects.variables.constant import Constants

# Create your views here.
def projects(request):
    msg = "Hello you are on the project page"
    context = {"message":msg}
    return render(request, 'projects/projects.html',context)


def project(request, pk):
    msg = "Hello you are on the project page"
    context = {"message":msg}
    return render(request, 'projects/single-project.html')
