from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models import Profile, User
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class CreateProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ["age", "gender"]


class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["email"]

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model =Profile
    fields = ["bio", "profile_picture_url", "match_distance", "match_gender"]




