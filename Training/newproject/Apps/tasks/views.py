from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Tasks_Views(request):
    return HttpResponse('Tasks page')