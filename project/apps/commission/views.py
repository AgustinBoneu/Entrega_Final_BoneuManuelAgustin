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


# def indexcommission (request: HttpRequest) -> HttpResponse:
#     return render(request, "commission/index_commission.html")  

class CommissionCreate(LoginRequiredMixin,CreateView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/create_commission.html"
    success_url = reverse_lazy("commission:index commission")

# def create_commission(request,): 
#     from .forms import CommissionForm
#     if request.method == "POST":
#         form = CommissionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("commission:index commission"))
#     else:  
#         form = CommissionForm()
#     return render(request, "commission/create_commission.html",{"form": form})

class InputCreate(LoginRequiredMixin,CreateView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/create_input.html"
    success_url = reverse_lazy("commission:index commission")

# def create_input(request): 
#     form = forms.InputForm(request.POST) 
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect("commission:index commission")
#     context = {"form": form}
#     return render (request,"commission/create_input.html",context)

class DiscountCreate(LoginRequiredMixin,CreateView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/create_discount.html"
    success_url = reverse_lazy("commission:index commission")

# def create_discount(request):  
#     form = forms.DiscountForm(request.POST)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect("commission:index commission")
#     context = {"form": form}
#     return render (request,"commission/create_discount.html",context)

class CommissionList(LoginRequiredMixin,ListView):
    model = Commissions_USF
    template_name = "commission/commission_list.html"
    # context_object_name = "categorias"
    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Commissions_USF.objects.filter(name_commission__icontains=query)
        else:
            object_list = Commissions_USF.objects.all()
        return object_list


# def commission_list(request):
#     categorias = Commissions_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/commission_list.html",context)

class DiscountList(LoginRequiredMixin,ListView):
    model = Discount_CommissionsBank_USF
    template_name = "commission/discount_list.html"
    # context_object_name = "categorias"

    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Discount_CommissionsBank_USF.objects.filter(name_client__icontains=query)
        else:
            object_list = Discount_CommissionsBank_USF.objects.all()
        return object_list


# def discount_list(request):
#     categorias = Discount_CommissionsBank_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/discount_list.html",context)

class InputList(LoginRequiredMixin,ListView):
    model = Input_Commissions_USF
    template_name = "commission/input_list.html"
    # context_object_name = "categorias"
    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = Input_Commissions_USF.objects.filter(date_of_entry__icontains=query)
        else:
            object_list = Input_Commissions_USF.objects.all()
        return object_list

# def input_list(request):
#     categorias = Input_Commissions_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/input_list.html",context)

class DeleteComission(LoginRequiredMixin,DeleteView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/deletecommission_list.html"
    success_url = reverse_lazy("commission:index commission")


# def delete_commission (request,id):
#     categoria = Commissions_USF.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("commission:index commission")
#     return render(request, "commission/deletecommission_list.html", {"categoria": categoria})

class DeleteInput(LoginRequiredMixin,DeleteView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/deleteinput_list.html"
    success_url = reverse_lazy("commission:index commission")

# def delete_input (request,id):
#     categoria = Input_Commissions_USF.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("commission:index commission")
#     return render(request, "commission/deleteinput_list.html", {"categoria": categoria})

class DeleteDiscount(LoginRequiredMixin,DeleteView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/deletediscount_list.html"
    success_url = reverse_lazy("commission:index commission")

# def delete_discount (request,id):
#     categoria = Discount_CommissionsBank_USF.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("commission:index commission")
#     return render(request, "commission/deletediscount_list.html", {"categoria": categoria})

class CommissionUpdate(LoginRequiredMixin,UpdateView):
    model = Commissions_USF
    forms_class = forms.CommissionForm
    fields = "__all__"
    template_name = "commission/updatecommission_list.html"
    success_url = reverse_lazy("commission:index commission")


# def update_commission(request, id):
#     categoria = Commissions_USF.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.CommissionForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("commission:index commission")
#     else:
#         form = forms.CommissionForm(instance=categoria)
#     return render(request, "commission/updatecommission_list.html", {"form": form})

class InputUpdate(LoginRequiredMixin,UpdateView):
    model = Input_Commissions_USF
    forms_class = forms.InputForm
    fields = "__all__"
    template_name = "commission/updateinput_list.html"
    success_url = reverse_lazy("commission:index commission")

# def update_input(request, id):
#     categoria = Input_Commissions_USF.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.InputForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("commission:index commission")
#     else:
#         form = forms.InputForm(instance=categoria)
#     return render(request, "commission/updateinput_list.html",{"form": form})

class DiscountUpdate(LoginRequiredMixin,UpdateView):
    model = Discount_CommissionsBank_USF
    forms_class = forms.DiscountForm
    fields = "__all__"
    template_name = "commission/updatediscount_list.html"
    success_url = reverse_lazy("commission:index commission")
        
# def update_discount(request, id):
#     categoria = Discount_CommissionsBank_USF.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.DiscountForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("commission:index commission")
#     else:
#         form = forms.DiscountForm(instance=categoria)
#     return render(request, "commission/updatediscount_list.html", {"form": form})

class CommissionDetail(DetailView): 
    model = Commissions_USF
    template_name = "commission/commissiondetail.html"

class InputDetail(DetailView): 
    model = Input_Commissions_USF
    template_name = "commission/inputdetail.html"

class DiscountDetail(DetailView): 
    model = Discount_CommissionsBank_USF
    template_name = "commission/discountdetail.html"











