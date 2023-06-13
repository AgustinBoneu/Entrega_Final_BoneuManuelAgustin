from django.urls import path
from . import views


urlpatterns = [
    path("index commission/", views.indexcommission, name="index commission"),
    path("create commission/", views.create_commission, name="create commission"),
    path("input commission/", views.create_input, name="input commission"),
    path("discount commission/", views.create_discount, name="discount commission"),
    path("list commission/", views.commission_list, name="list commission"),
    path("list input/", views.input_list, name="list input"),
    path("list discount/", views.discount_list, name="list discount"),
    path("deletecommission_list/<int:id>", views.delete_commission, name="deletecommission_list"),
    path("deletediscount_list/<int:id>", views.delete_discount, name="deletediscount_list"),
    path("deleteinput_list/<int:id>", views.delete_input, name="deleteinput_list"),
    path("updatecommission_list/<int:id>", views.update_commission, name="updatecommission_list"),
    path("updateinput_list/<int:id>", views.update_input, name="updateinput_list"),
    path("updatediscount_list/<int:id>", views.update_discount, name="updatediscount_list"),
]

    