from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'diary_entry/home.html')

def entry(request):
    return render('diary_entry/entry_page.html')
