from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexhome, name="index home"),

]
