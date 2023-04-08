from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')

def entry(request):
    return HttpResponse('diary entry')
