from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .templates.forms import CreateUserForm, UpdateUserForm, UpdateProfileForm
import os
from django.conf import settings
from .utils.face_blurrer import make_blurred_picture
from .utils.geolocation import get_geolocation, get_ip
from .models import Profile
# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  user = request.user
  profile = user.profile
  profile_details = {
  'bio': profile.bio,
  }
  user_details = {
    'email': user.email
  }
  update_user_form = UpdateUserForm()
  if request.method == 'POST':
    update_user_form = UpdateUserForm(request.POST,  instance=user)
    update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance = profile)
    if update_user_form.is_valid() and update_profile_form.is_valid():
      user = update_user_form.save()
      profile = update_profile_form.save(commit = False)
      blurred_picture_url = make_blurred_picture(profile.profile_picture_url.url)
      profile.blurred_profile_picture_url = blurred_picture_url
      profile.save()
  else:
    update_user_form = UpdateUserForm()
    update_profile_form = UpdateProfileForm()
  context = {'update_user_form': update_user_form, 'update_profile_form': update_profile_form}
  return render(request, 'edit_profile_view.html',context)

  

  context = {'form' : form}
  return render(request, "edit_profile_view.html", context)
# @login_required
def swipe_view(request, *args, **kwargs):
  return render(request, "swipe_view.html", {})

  return render(request, "swipe_view.html", {})
# @login_required
def settings_view(request, *args, **kwargs):
  return render(request, "settings_view.html", {})
# @login_required
def faq_view(request, *args, **kwargs):
  return render(request, "faq_view.html", {})

def landing_view(request):
  return render(request, "landing_view.html", {})

def register_view(request, *args, **kwargs):

  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request, f"User has been created for {user.username}")
      return redirect('/login/')
  else:
    form = CreateUserForm()

  context = {'form': form}
  return render(request, "register_view.html", context)

def login_view(request, *args, **kwargs):
  if request.method == "POST":
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
      user = form.get_user()
      set_profile_location(request, user)
      login(request, user)
      return redirect('/app/')
  else:
    form = AuthenticationForm(request)
  context = {'form': form}
  return render(request, 'login_view.html',context)

def logout_user(request,*args, **kwargs):
  logout(request)
  return redirect('/')





def set_profile_location(request, user):
  profile = user.profile
  location_data = get_geolocation(request)
  profile.city = location_data['city']
  profile.latitude = location_data['latitude']
  profile.longitude = location_data['longitude']
  profile.save()



