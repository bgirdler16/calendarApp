# accounts/urls.py updated by Tyzer 11/8/22

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]