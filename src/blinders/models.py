from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  # ip_address = models.CharField(max_length=20, null=True)
  age = models.IntegerField(null=True, blank=False)
  # profile_picture_url = models.ImageField(null = True, blank = True, upload_to = "images/")
  # blurred_profile_picture_url = models.ImageField(null = True, blank = True,upload_to = "images/")
  # description = models.TextField(default = "Description")

class Profile(models.Model):
  
  # ip_address = models.CharField(max_length=20, null=True)
  # profile_picture_url = models.ImageField(null = True, blank = True, upload_to = "images/")
  # blurred_profile_picture_url = models.ImageField(null = True, blank = True,upload_to = "images/")
  # description = models.TextField(default = "Description")



    


