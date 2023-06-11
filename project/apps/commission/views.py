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
        return redirect("index")
    context = {"form": form}
    return render (request,"commission/create_input.html",context)

def create_discount(request):  
    form = forms.DiscountForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("commission:index commission")
    context = {"form": form}
    return render (request,"commission/create_discount.html",context)


