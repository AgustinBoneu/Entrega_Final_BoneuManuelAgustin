from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexhome, name="index home"),
    path("about/", views.abouthome, name="about"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout")
]
urlpatterns += staticfiles_urlpatterns()

