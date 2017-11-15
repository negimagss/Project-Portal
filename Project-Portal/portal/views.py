from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def index(request):
    return render(request, 'index.html') #context is data which is not required 

