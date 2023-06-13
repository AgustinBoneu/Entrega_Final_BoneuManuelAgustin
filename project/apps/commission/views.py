from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Commissions_USF,Input_Commissions_USF,Discount_CommissionsBank_USF
from . import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def indexcommission (request):
    return render(request, 'commission/index_commission.html')  

class CommissionCreate(CreateView):
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

class InputCreate(CreateView):
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

class DiscountCreate(CreateView):
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

class CommissionList(ListView):
    model = Commissions_USF
    template_name = "commission/commission_list.html"
    context_object_name = "categorias"


# def commission_list(request):
#     categorias = Commissions_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/commission_list.html",context)

class DiscountList(ListView):
    model = Discount_CommissionsBank_USF
    template_name = "commission/discount_list.html"
    context_object_name = "categorias"


# def discount_list(request):
#     categorias = Discount_CommissionsBank_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/discount_list.html",context)

class InputList(ListView):
    model = Input_Commissions_USF
    template_name = "commission/input_list.html"
    context_object_name = "categorias"

# def input_list(request):
#     categorias = Input_Commissions_USF.objects.all()
#     context = {"categorias": categorias}
#     return render (request,"commission/input_list.html",context)

class DeleteComission(DeleteView):
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

class DeleteInput(DeleteView):
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

class DeleteDiscount(DeleteView):
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

class CommissionUpdate(UpdateView):
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

class InputUpdate(UpdateView):
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

class DiscountUpdate(UpdateView):
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









