from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import os
from  django.conf import settings

class User(AbstractUser):
  age = models.IntegerField(null=True, blank=False)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  city = models.CharField(max_length=30, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, null = True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, null = True)
  age = models.IntegerField(null=True, blank=False)
  bio = models.TextField(max_length=5000, default = "Add a bio", null = True)
  profile_picture_url = models.ImageField(default = os.path.join( "images","default_profile_picture.jpg"), blank = True, upload_to = "images/")
  blurred_profile_picture_url = models.ImageField(default = os.path.join( "images","default_profile_picture.jpg"), blank = True, upload_to = "images/")



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




    


