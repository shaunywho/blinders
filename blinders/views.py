from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .templates.forms import CreateUserForm, UpdateUserForm
# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  user = request.user
  user_details = {
  'description': user.description,
  'profile_pic': user.profile_pic,
  }
  form = UpdateUserForm(initial=user_details)
  if request.method == 'POST':
    form = UpdateUserForm(request.POST, request.FILES, instance=user)
    if form.is_valid():

      description = form.cleaned_data.get('description')
      profile_pic = form.cleaned_data.get('profile_pic')
      print(profile_pic)
      user = form.save()
      user.save()
  context = {'form': form}
  print(form.errors)
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
      login(request, user)
      return redirect('/app/')
  else:
    form = AuthenticationForm(request)
  context = {'form': form}
  return render(request, 'login_view.html',context)

def logout_user(request,*args, **kwargs):
  logout(request)
  return redirect('/')


