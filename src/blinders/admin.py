from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# Register your models here.

from .models import Profile, Match
admin.site.register(Profile)
admin.site.register(Match)