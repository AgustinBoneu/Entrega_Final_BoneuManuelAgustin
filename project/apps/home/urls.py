from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexhome, name="index home"),
    path("about/", views.abouthome, name="about"),
    path("login/", views.login_request, name="login"),
]
urlpatterns += staticfiles_urlpatterns()

