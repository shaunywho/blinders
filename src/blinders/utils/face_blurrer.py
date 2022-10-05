from django.conf import settings
import cv2 
import os

def make_blurred_picture(picture_url):
  unblurred_picture_full_url = f"{settings.BASE_DIR}{picture_url}"
  image = cv2.imread(unblurred_picture_full_url) 
  face_cascade = cv2.CascadeClassifier(os.path.join(settings.ASSETS_URL,"opencv","haarcascade_frontalface_default.xml"))
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  for face in faces:
    x ,y ,w, h = face
    face_img = image[y:y+h,x:x+h]
    blurred_face_img =cv2.blur(face_img, (100,100))
    image[y:y+h,x:x+h] = blurred_face_img
  blurred_picture_url = make_blurred_picture_url(picture_url)
  blurred_picture_full_url =f"{settings.BASE_DIR}{blurred_picture_url}"
  print(blurred_picture_full_url)
  cv2.imwrite(blurred_picture_full_url, image)
  return blurred_picture_url

def make_blurred_picture_url(picture_url):
  directory = os.path.dirname(picture_url)
  base = os.path.basename(picture_url)
  filename, extension = os.path.splitext(base)
  return os.path.join(directory, f"{filename}_blurred{extension}")


  