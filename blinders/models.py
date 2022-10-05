from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import cv2 
import os
class User(AbstractUser):
  location = models.CharField(max_length=30, blank=True)
  age = models.IntegerField(null=True, blank=False)
  profile_picture_url = models.ImageField(null = True, blank = True, upload_to = "images/")
  blurred_profile_picture_url = models.ImageField(null = True, blank = True,upload_to = "images/")
  description = models.TextField(default = "Description")

  def blur_picture(self, picture_url):

    image = cv2.imread(picture_url) 
    face_cascade = cv2.CascadeClassifier(os.path.join(settings.ASSETS_URL,"haarcascade_frontalface_default.xml"))
    


