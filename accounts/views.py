from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomCreatonForm

class RegisterView(CreateView):
    form_class = CustomCreatonForm
    template_name = 'accounts/register.html'
    success_url = 'reverse_lazy("login")'
