from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('diary_entry', views.entry, name="diary_entry")
]