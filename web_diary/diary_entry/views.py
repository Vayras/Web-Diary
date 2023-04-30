from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .models import *
from .forms import EntryForm
from .filters import EntryFilter

# Create your views here.

def home(request): 

    entries = Entry.objects.all()

    total_entries = entries.count()

    myFilter = EntryFilter(request.GET, queryset=entries)
    entries = myFilter.qs

    context = {'total_entries':total_entries, 'entries': entries, 'myFilter':myFilter}

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

def PreviewEntry(request, pk):
    entry_info = get_object_or_404(Entry, id=pk)

    form = EntryForm(instance=entry_info)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry_info)

        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request, 'diary_entry/entry_form.html', context)

def deleteEntry(request):

    context = {}

    return render(request, 'diary_entry/delete.html', context)

def login(request):
    return render(request, 'diary_entry/sign_in.html')

def register(request):
    return render(request, 'diary_entry/registration_page.html')