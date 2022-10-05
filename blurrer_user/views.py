from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pprint import pprint
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

def landing_view(request, *args, **kwargs):
  return render(request, "landing_view.html", {})

  
