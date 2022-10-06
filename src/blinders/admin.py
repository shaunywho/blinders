from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# Register your models here.

from .models import User, Profile
admin.site.register(User)
admin.site.register(Profile)