from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Commissions_USF,Input_Commissions_USF,Discount_CommissionsBank_USF
from . import forms


# Create your views here.
def indexcommission (request):
    return render(request, 'commission/index_commission.html')  

def create_commission(request,): 
    from .forms import CommissionForm
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("commission:index commission"))
    else:  
        form = CommissionForm()
    return render(request, "commission/create_commission.html",{"form": form})

def create_input(request): 
    form = forms.InputForm(request.POST) 
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("commission:index commission")
    context = {"form": form}
    return render (request,"commission/create_input.html",context)

def create_discount(request):  
    form = forms.DiscountForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("commission:index commission")
    context = {"form": form}
    return render (request,"commission/create_discount.html",context)


def commission_list(request):
    categorias = Commissions_USF.objects.all()
    context = {"categorias": categorias}
    return render (request,"commission/commission_list.html",context)

def discount_list(request):
    categorias = Discount_CommissionsBank_USF.objects.all()
    context = {"categorias": categorias}
    return render (request,"commission/discount_list.html",context)

def input_list(request):
    categorias = Input_Commissions_USF.objects.all()
    context = {"categorias": categorias}
    return render (request,"commission/input_list.html",context)

def delete_commission (request,id):
    categoria = Commissions_USF.objects.get(id=id)
    if request.method == "POST":
        categoria.delete()
        return redirect("commission:index commission")
    return render(request, "commission/deletecommission_list.html", {"categoria": categoria})

def delete_input (request,id):
    categoria = Input_Commissions_USF.objects.get(id=id)
    if request.method == "POST":
        categoria.delete()
        return redirect("commission:index commission")
    return render(request, "commission/deleteinput_list.html", {"categoria": categoria})

def delete_discount (request,id):
    categoria = Discount_CommissionsBank_USF.objects.get(id=id)
    if request.method == "POST":
        categoria.delete()
        return redirect("commission:index commission")
    return render(request, "commission/deletediscount_list.html", {"categoria": categoria})

def update_commission(request, id):
    categoria = Commissions_USF.objects.get(id=id)
    if request.method == "POST":
        form = forms.CommissionForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("commission:index commission")
    else:
        form = forms.CommissionForm(instance=categoria)
    return render(request, "commission/updatecommission_list.html", {"form": form})

def update_input(request, id):
    categoria = Input_Commissions_USF.objects.get(id=id)
    if request.method == "POST":
        form = forms.InputForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("commission:index commission")
    else:
        form = forms.InputForm(instance=categoria)
    return render(request, "commission/updateinput_list.html",{"form": form})
        
def update_discount(request, id):
    categoria = Discount_CommissionsBank_USF.objects.get(id=id)
    if request.method == "POST":
        form = forms.DiscountForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("commission:index commission")
    else:
        form = forms.DiscountForm(instance=categoria)
    return render(request, "commission/updatediscount_list.html", {"form": form})









