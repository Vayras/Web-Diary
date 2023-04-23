from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):

    entry = Entry.objects.all()

    context = {'entry':entry}

    return render(request, 'diary_entry/home.html', context)

def entry(request):
    return render(request, 'diary_entry/entry_form.html')

def login(request):
    return render(request, 'diary_entry/sign_in.html')

def register(request):
    return render(request, 'diary_entry/registration_page.html')