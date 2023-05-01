from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .models import *
from .forms import EntryForm, CreateUserForm
from .filters import EntryFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
# we cannot access the home page unless we have logged in otherwise we will be directed back to the login page.
def home(request): 

    entries = Entry.objects.all()

    total_entries = entries.count()

    myFilter = EntryFilter(request.GET, queryset=entries)
    entries = myFilter.qs

    context = {'total_entries':total_entries, 'entries': entries, 'myFilter':myFilter}

    return render(request, 'diary_entry/home.html', context)

@login_required(login_url='login')
def entry(request):
    form = EntryForm

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'diary_entry/entry_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteEntry(request):

    context = {}

    return render(request, 'diary_entry/delete.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.info(request, 'Username or password is incorrect.')

        return render(request, 'diary_entry/sign_in.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +  user)
                return redirect('login')                                                   
        
        context={'form':form}

        return render(request, 'diary_entry/registration_page.html', context)