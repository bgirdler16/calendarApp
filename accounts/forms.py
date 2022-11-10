# accounts/forms.py Updated by Tyzer on 11/8/22

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CustomUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        Fields = (
            "username",
            "email",
            "age",
        )