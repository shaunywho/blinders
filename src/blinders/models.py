from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  location = models.CharField(max_length=30, blank=True)
  age = models.IntegerField(null=True, blank=False)
  profile_picture_url = models.ImageField(null = True, blank = True, upload_to = "images/")
  blurred_profile_picture_url = models.ImageField(null = True, blank = True,upload_to = "images/")
  description = models.TextField(default = "Description")


    


