# accounts/views.py updated by Tyzer on 11/8/22

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class signUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"