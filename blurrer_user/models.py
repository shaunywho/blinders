from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.TextField(default = "First Name")
  last_name = models.TextField(default = "Last Name")
  age = models.SmallIntegerField()
  profile_picture = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  blurred_profile_picture = models.ImageField(default = "/Users/shaun/Projects/blinders/src/profile_picture.jpeg")
  description = models.TextField(default = "Description")
  summary = models.TextField(default = "Summary")