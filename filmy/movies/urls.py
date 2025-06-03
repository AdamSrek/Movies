from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from movies import views

urlpatterns = [
    path('', views.seznam_filmu, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
