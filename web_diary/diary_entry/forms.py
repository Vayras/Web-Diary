from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry

class EntryForm(ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"class":"text-gray-700  h-[4rem] text-3xl focus:outline-none  w-full pl-4 placeholder:flex placeholder:flex-col placeholder:justify-center   placeholder:text-3xl placeholder:text-gray-700"
    , "placeholder":"Title"}))

    mood = forms.CharField(label="Mood", widget=forms.TextInput(attrs={"class":"text-gray-700  h-[3.2rem] text-xl focus:outline-none  w-full pl-4 placeholder:flex placeholder:flex-col placeholder:justify-center   placeholder:text-xl placeholder:text-gray-700"
    , "placeholder":"Mood of the day"}))

    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={"class":"resize-none w-full h-[52.5rem] focus:outline-none p-4", "placeholder":"Dear Diary..."}))

    class Meta:
        model = Entry
        fields = '__all__'

class CreateUserForm(UserCreationForm):

    username = forms.CharField(label="name",widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5', 'placeholder':'name'}))

    email = forms.CharField(label="email",widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5', 'placeholder':'username@gmail.com'}))

    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5', 'placeholder':'••••••••'}))

    password2 = forms.CharField(label="re-password",widget=forms.PasswordInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5', 'placeholder':'••••••••'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']