from django.urls import path
from . import views

urlpatterns = [
    path("index commission/", views.IndexViews.as_view(), name="index commission"),
    path("create commission/", views.CommissionCreate.as_view(), name="create commission"),
    path("input commission/", views.InputCreate.as_view(), name="input commission"),
    path("discount commission/", views.DiscountCreate.as_view(), name="discount commission"),
    path("list commission/", views.CommissionList.as_view(), name="list commission"),
    path("list input/", views.InputList.as_view(), name="list input"),
    path("list discount/", views.DiscountList.as_view(), name="list discount"),
    path("deletecommission_list/<int:pk>", views.DeleteComission.as_view() , name="deletecommission_list"),
    path("deletediscount_list/<int:pk>", views.DeleteDiscount.as_view(), name="deletediscount_list"),
    path("deleteinput_list/<int:pk>", views.DeleteInput.as_view(), name="deleteinput_list"),
    path("updatecommission_list/<int:pk>", views.CommissionUpdate.as_view(), name="updatecommission_list"),
    path("updateinput_list/<int:pk>", views.InputUpdate.as_view(), name="updateinput_list"),
    path("updatediscount_list/<int:pk>", views.DiscountUpdate.as_view(), name="updatediscount_list"),
    path("commission_detail/<int:pk>", views.CommissionDetail.as_view(), name="commission_detail"),
    path("input_detail/<int:pk>", views.InputDetail.as_view(), name="input_detail"),
    path("discount_detail/<int:pk>", views.DiscountDetail.as_view(), name="discount_detail"),
]
