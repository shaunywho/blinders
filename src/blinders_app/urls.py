"""blinders_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from blinders.views import edit_profile_view, find_match_view, settings_view, faq_view, landing_view, register_view, login_view, logout_user, matches_view, make_like

urlpatterns = [
    path('', landing_view, name = 'home'),
    path('app/edit-profile/', edit_profile_view),
    path('app/', find_match_view, name = 'swipe_page'),
    path('app/settings/', settings_view),
    path('app/faq', faq_view),
    path('admin/', admin.site.urls),
    path('logout/', logout_user),
    path("register/", register_view),
    path("login/", login_view),
    path("app/matches", matches_view),
    path("swipe/<int:id>/<int:like>", make_like, name = "swipe_profile"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
