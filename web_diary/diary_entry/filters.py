import django_filters
from django_filters.filters import DateFilter
from .models import *

class EntryFilter(django_filters.FilterSet):

    class Meta:
        model = Entry
        fields = ['date_created']