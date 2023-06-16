from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import Commissions_USF,Input_Commissions_USF,Discount_CommissionsBank_USF
from . import forms
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexViews(TemplateView):
    template_name = "commission/index_commission.html"

class CommissionCreate(LoginRequiredMixin,CreateView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/create_commission.html"
    success_url = reverse_lazy("commission:index commission")

class InputCreate(LoginRequiredMixin,CreateView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/create_input.html"
    success_url = reverse_lazy("commission:index commission")

class DiscountCreate(LoginRequiredMixin,CreateView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/create_discount.html"
    success_url = reverse_lazy("commission:index commission")

class CommissionList(LoginRequiredMixin,ListView):
    model = Commissions_USF
    template_name = "commission/commission_list.html"
    
    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Commissions_USF.objects.filter(name_commission__icontains=query)
        else:
            object_list = Commissions_USF.objects.all()
        return object_list

class DiscountList(LoginRequiredMixin,ListView):
    model = Discount_CommissionsBank_USF
    template_name = "commission/discount_list.html"
   
    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Discount_CommissionsBank_USF.objects.filter(name_client__icontains=query)
        else:
            object_list = Discount_CommissionsBank_USF.objects.all()
        return object_list

class InputList(LoginRequiredMixin,ListView):
    model = Input_Commissions_USF
    template_name = "commission/input_list.html"
    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Input_Commissions_USF.objects.filter(date_of_entry__icontains=query)
        else:
            object_list = Input_Commissions_USF.objects.all()
        return object_list

class DeleteComission(LoginRequiredMixin,DeleteView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/deletecommission_list.html"
    success_url = reverse_lazy("commission:index commission")

class DeleteInput(LoginRequiredMixin,DeleteView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/deleteinput_list.html"
    success_url = reverse_lazy("commission:index commission")

class DeleteDiscount(LoginRequiredMixin,DeleteView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/deletediscount_list.html"
    success_url = reverse_lazy("commission:index commission")

class CommissionUpdate(LoginRequiredMixin,UpdateView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/updatecommission_list.html"
    success_url = reverse_lazy("commission:index commission")

class InputUpdate(LoginRequiredMixin,UpdateView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/updateinput_list.html"
    success_url = reverse_lazy("commission:index commission")

class DiscountUpdate(LoginRequiredMixin,UpdateView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/updatediscount_list.html"
    success_url = reverse_lazy("commission:index commission")
        
class CommissionDetail(DetailView): 
    model = Commissions_USF
    template_name = "commission/commissiondetail.html"

class InputDetail(DetailView): 
    model = Input_Commissions_USF
    template_name = "commission/inputdetail.html"

class DiscountDetail(DetailView): 
    model = Discount_CommissionsBank_USF
    template_name = "commission/discountdetail.html"
