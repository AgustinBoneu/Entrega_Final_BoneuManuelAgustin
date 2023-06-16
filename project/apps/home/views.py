from django.shortcuts import  render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def indexhome (request):
    return render(request, 'home/index_home.html')  
def abouthome (request):
    return render(request, 'home/about.html')  

@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index_home.html", {"menssage": "Usuario creado 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})
