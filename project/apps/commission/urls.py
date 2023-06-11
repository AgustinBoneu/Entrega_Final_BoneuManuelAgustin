from django.urls import path
from . import views


urlpatterns = [
    path("index commission/", views.indexcommission, name="index commission"),
    path("create commission/", views.create_commission, name="create commission"),
    path("input commission/", views.create_input, name="input commission"),
    path("discount commission/", views.create_discount, name="discount commission"),
]
