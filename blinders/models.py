from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  age = models.SmallIntegerField()
  profile_picture = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  blurred_profile_picture = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  description = models.TextField(default = "Description")
  summary = models.TextField(default = "Summary")