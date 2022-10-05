from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  location = models.CharField(max_length=30, blank=True)
  age = models.IntegerField(null=True, blank=False)
  profile_pic = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  blurred_profile_picture = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  description = models.TextField(default = "Description")

