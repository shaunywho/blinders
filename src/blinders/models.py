from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import os
from  django.conf import settings

MIN_AGE = 18
MAX_AGE =99




class Profile(models.Model):

  class MatchGenderChoices(models.TextChoices):
    FEMALE = 'FEMALE'
    MALE = 'MALE'
    ALL = 'ALL'

  class GenderChoices(models.TextChoices):
      FEMALE = 'FEMALE'
      MALE = 'MALE'
      NONBINARY = 'NONBINARY'
  display_name = models.CharField(max_length=30, null=True)
  age = models.IntegerField(null=True, blank=False)
  gender = models.CharField(max_length=10, choices = GenderChoices.choices, null = True, blank = False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  liked_profiles = models.ManyToManyField('self', through= 'Match')
  match_distance = models.IntegerField(default = 30)
  match_age_max = models.IntegerField(default = 99)
  match_age_min = models.IntegerField(default = 18)
  match_gender =  models.CharField(max_length=10, choices = MatchGenderChoices.choices, null = True, blank = False)

  city = models.CharField(max_length=30, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, null = True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, null = True)
  age = models.IntegerField(null=True, blank=False,validators=[MinValueValidator(MIN_AGE), MaxValueValidator(MAX_AGE)])
  bio = models.TextField(max_length=5000, default = "Add a bio", null = True)
  profile_picture_url = models.ImageField(default = os.path.join( "media", "images","default_profile_picture.jpg"), blank = True, upload_to = "images/")
  blurred_profile_picture_url = models.ImageField(default = os.path.join( "media", "images","default_profile_picture.jpg"), blank = True, upload_to = "images/")
 



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Match(models.Model):
  swiper = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "swiper")
  swipee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "swipee", null = True)
  liked = models.BooleanField(null=True)
  match = models.BooleanField(default= False)
  date_liked= models.DateTimeField(auto_now=True)
  date_confirmed =models.DateTimeField(null= True, blank = True)
  class Meta:
    unique_together = [['swiper', 'swipee']]

class Message(models.Model):
  match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  message = models.TextField(blank = False, null = False)



    


