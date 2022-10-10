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
from .models import Profile, Match, Message
from django.contrib.auth.models import User
from django.db.models import Exists, OuterRef, Q
from django.forms.models import model_to_dict
from django.urls import reverse
import datetime


# Create your views here.
# @login_required
def edit_profile_view(request, *args, **kwargs):
  profile = request.user.profile
  current_profile_picture_url = profile.profile_picture_url
  profile_details = {
  'bio': profile.bio,
  }
  if request.method == 'POST':
    update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance = profile)
    if update_profile_form.is_valid():
      profile = update_profile_form.save()
      if current_profile_picture_url!= profile.profile_picture_url:
        profile_picture_url = profile.profile_picture_url.url
        blurred_picture_url = make_blurred_picture(profile_picture_url)
        profile.profile_picture_url = profile_picture_url
        profile.blurred_profile_picture_url = blurred_picture_url
        profile.save()
  else:
    update_profile_form = UpdateProfileForm(initial= profile_details)
  context = {'update_profile_form': update_profile_form}
  return render(request, 'edit_profile_view.html',context)

# @login_required
def find_match_view(request, *args, **kwargs):
  profile = request.user.profile
  profiles = [generate_card(profile,match_profile) for match_profile in get_profiles(profile)]
  context = {'profiles': profiles}
  return render(request, "find_match_view.html", context)

def make_like(request,**kwargs):
  like_true = bool(kwargs.get('like'))
  user = request.user
  match_profile_id = kwargs.get('id')
  liked = Match.objects.filter(liker_id=match_profile_id)

  if liked:
    Match.date_confirmed = datetime.datetime.now()
    Match.match = like_true
  else:

    match = Match(liker_id = user.profile.id, likee_id = match_profile_id)
    match.save()
  return redirect('swipe_page')




    

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
      profile.display_name = user.first_name
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



def get_profiles(profile):
  # returns list of profiles where the age and genders match the user's choices
  if profile.match_gender == 'ALL':
    matches = Profile.objects.exclude(id = profile.id, liker_id=profile.id).filter(Q(age__lte=profile.match_age_max) & Q(age__gte=profile.match_age_min))
    
  else:
    matches = Profile.objects.exclude(id = profile.id, liker_id=profile.id ).filter(Q(age__lte=profile.match_age_max) & Q(age__gte=profile.match_age_min) & Q(gender=profile.match_gender))
  # print(Profile.objects.exclude(id = profile.id).filter(Q(age__lte=profile.match_age_max) & Q(age__gte=profile.match_age_min)))
  print(matches)
  matches = [match_profile for match_profile in matches if get_distance(match_profile.latitude,match_profile.longitude,profile.latitude, profile.longitude)<profile.match_distance]

  return matches

def generate_card(profile,match_profile):
  match_profile_card = model_to_dict(match_profile,fields =['display_name', 'age', 'bio', 'gender','blurred_profile_picture_url', 'id'])
  match_profile_card['like_url'] = reverse('swipe_profile',args =[match_profile.id,1])
  match_profile_card['reject_url'] = reverse('swipe_profile',args =[match_profile.id,0])
  match_profile_card['distance'] = get_distance(match_profile.latitude,match_profile.longitude,profile.latitude, profile.longitude)
  return match_profile_card



  


