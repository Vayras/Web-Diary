from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('entry/', views.entry, name="entry"),
    path('preview/<int:pk>/', views.PreviewEntry, name="preview"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
]