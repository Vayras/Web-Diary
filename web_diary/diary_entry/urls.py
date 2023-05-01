from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name="home"),
    path('entry/', views.entry, name="entry"),
    path('preview/<int:pk>/', views.PreviewEntry, name="preview"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.register, name="register")
]