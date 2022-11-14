# accounts/urls.py updated by Tyzer 11/8/22

from django.urls import path
from .views import signUpView

urlpatterns = [
    path("signup/", signUpView.as_view(), name="signup"),
]