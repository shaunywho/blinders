from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .templates.forms import CreateUserForm, CreateProfileForm, UpdateUserForm, UpdateProfileForm
import os
from django.conf import settings
from .utils.face_blurrer import make_blurred_picture
from .utils.geolocation import get_geolocation, get_ip, get_distance
from .models import Profile
from django.contrib.auth.models import User
from django.db.models import Exists, OuterRef, Q


# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  profile = request.user.profile
  profile_details = {
  'bio': profile.bio,
  }
  if request.method == 'POST':
    update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance = profile)
    if update_profile_form.is_valid():
      profile = update_profile_form.save(commit = False)
      print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      print(profile.profile_picture_url.path)
      print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      blurred_picture_url = make_blurred_picture(profile.profile_picture_url.url)
      profile.blurred_profile_picture_url = blurred_picture_url
      profile.save()
  else:
    update_profile_form = UpdateProfileForm(initial= profile_details)
  context = {'update_profile_form': update_profile_form}
  return render(request, 'edit_profile_view.html',context)

# @login_required
def find_match_view(request, *args, **kwargs):
  user = request.user
  profiles = get_profiles_age_gender(user)
  print(profiles)
  context = {'profiles': profiles}
  return render(request, "find_match_view.html", context)

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
    create_user_form = CreateUserForm(request.POST)
    create_profile_form = CreateProfileForm(request.POST)
    if create_user_form.is_valid() and create_profile_form.is_valid():
      user = create_user_form.save()
      profile = user.profile
      profile.first_name = user.first_name
      profile.age = create_profile_form.cleaned_data['age']
      profile.gender = create_profile_form.cleaned_data['gender']
      profile.save()
      messages.success(request, f"User has been created for {user.username}")
      return redirect('/login/')
  else:
    create_user_form = CreateUserForm()
    create_profile_form = CreateProfileForm()


  context = {'create_user_form': create_user_form, 'create_profile_form': create_profile_form}
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

def matches_view (request, *args, **kwargs):
  return render(request, 'matches_view.html')


def swipe_profile(request, *args, **kwargs):
  return redirect('find_match_view')



def set_profile_location(request, user):
  profile = user.profile
  location_data = get_geolocation(request)
  profile.city = location_data['city']
  profile.latitude = location_data['latitude']
  profile.longitude = location_data['longitude']
  profile.save()



def get_profiles_age_gender(user):
  profile = user.profile
  matches_age = Profile.objects.exclude(user = user).filter(age__lte=profile.match_age_max).filter(age__gte=profile.match_age_min)
  if profile.match_gender != 'ALL':
    matches_age_gender =  matches_age.filter(gender=profile.match_gender)
  else:
    matches_age_gender = matches_age
  return matches_age_gender

  

def get_profiles_age_gender_distance(user):
  user_profile = user.profile
  age_gender_matches = get_profiles_age_gender(user)
  matches_age_gender_distance = [match_profile for match_profile in age_gender_matches if get_distance(match_profile.latitude,match_profile.longitude,user_profile.latitude, user_profile.longitude)]
  return matches_age_gender_distance

