from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect

from message.forms import RegisterUserForm, LoginUserForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'message/base.html'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'message/register.html'
    success_url = reverse_lazy('message:home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'message/login.html'


    def get_success_url(self):
        return reverse_lazy('message:home')

def LogoutUser(request):
    logout(request)

    return redirect('message:home')