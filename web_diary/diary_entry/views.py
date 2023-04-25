from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import EntryForm

# Create your views here.

def home(request):

    entry = Entry.objects.all()

    total_entries = entry.count()

    context = {'entry':entry, 'total_entries':total_entries}

    return render(request, 'diary_entry/home.html', context)

def entry(request):
    form = EntryForm

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'diary_entry/entry_form.html', context)

def login(request):
    return render(request, 'diary_entry/sign_in.html')

def register(request):
    return render(request, 'diary_entry/registration_page.html')