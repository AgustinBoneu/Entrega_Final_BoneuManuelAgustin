from django.urls import path
from . import views

urlpatterns = [
    path("index user/", views.IndexViews.as_view(), name="index user"),

]
