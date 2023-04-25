from django import forms
from django.forms import ModelForm, widgets
from .models import Entry

class EntryForm(ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"class":"text-gray-700  h-[4rem] text-3xl focus:outline-none  w-full pl-4 placeholder:flex placeholder:flex-col placeholder:justify-center   placeholder:text-3xl placeholder:text-gray-700"
    , "placeholder":"Title"}))

    mood = forms.CharField(label="Mood", widget=forms.TextInput(attrs={"class":"text-gray-700  h-[3.2rem] text-xl focus:outline-none  w-full pl-4 placeholder:flex placeholder:flex-col placeholder:justify-center   placeholder:text-xl placeholder:text-gray-700"
    , "placeholder":"Mood of the day"}))

    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={"class":"resize-none w-full h-[52.5rem]   focus:outline-none p-4", "placeholder":"Dear Diary..."}))

    class Meta:
        model = Entry
        fields = '__all__'