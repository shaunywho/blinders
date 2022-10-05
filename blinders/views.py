from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .templates.forms import CreateUserForm
# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  return render(request, "edit_profile_view.html", {})
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
  form = CreateUserForm()
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request, f"User has been created for {user.username}")
      return redirect('/login/')

  context = {'form': form}
  return render(request, "register_view.html", context)

def login_view(request, *args, **kwargs):
  form = AuthenticationForm()
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      return redirect('/app/')
  context = {'form': form}
  return render(request, 'login_view.html',context)

