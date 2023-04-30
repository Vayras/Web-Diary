import django_filters 
from django_filters import DateFilter
from django import forms
from .models import *

class EntryFilter(django_filters.FilterSet):

    date_created = DateFilter(lookup_expr='icontains', label='', widget=forms.DateInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:outline focus:border-blue-500 block w-40 pl-10 p-2.5', 'placeholder': 'MM/DD/YYYY','style': 'width: 140px;'}))

    class Meta:
        model = Entry
        fields = ['date_created']