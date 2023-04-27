import django_filters
from django_flatpickr.widgets import DatePickerInput
from .models import *

class EntryFilter(django_filters.FilterSet):

    

    class Meta:
        model = Entry
        fields = ['date_created']