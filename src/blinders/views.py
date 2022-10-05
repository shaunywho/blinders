from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .templates.forms import CreateUserForm, UpdateUserForm
import os
from django.conf import settings
from .utils.face_blurrer import make_blurred_picture
# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  user = request.user

  
  
  user_details = {
  'description': user.description,
  }
  form = UpdateUserForm(initial=user_details)
  if request.method == 'POST':
    form = UpdateUserForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
      user = form.save()
      blurred_picture_url = make_blurred_picture(user.profile_picture_url.url)
      user.blurred_profile_picture_url = blurred_picture_url
      user.save()
  context = {'form': form}
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
  print(request.META.get('REMOTE_ADDR'))
  return render(request, "landing_view.html", {})

def register_view(request, *args, **kwargs):

  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.profile_picture_url = os.path.join(settings.MEDIA_ROOT, "default_profile_picture.jpeg")
      user.blurred_profile_picture_url= os.path.join(settings.MEDIA_ROOT, "default_profile_picture.jpeg")

      user.save()
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
      login(request, user)
      return redirect('/app/')
  else:
    form = AuthenticationForm(request)
  context = {'form': form}
  return render(request, 'login_view.html',context)

def logout_user(request,*args, **kwargs):
  logout(request)
  return redirect('/')


