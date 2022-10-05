from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from ..models import User
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'age']

class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["description", "profile_picture_url"]




