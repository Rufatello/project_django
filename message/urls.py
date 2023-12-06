from django.contrib import admin
from django.urls import path
from . import views
from message.apps import MessageConfig

app_name = MessageConfig.name

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser, name='logout'),
]