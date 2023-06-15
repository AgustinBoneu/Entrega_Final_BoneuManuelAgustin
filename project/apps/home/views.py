from django.shortcuts import  render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
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



def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'home/index_home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {"form": form})


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




# def register (request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = UserCreationForm(request, data=request.POST)
#         if form.is_valid():
#             usuar_name = form.cleaned_data.get("username")
#             form.save()
#             return render(request, "home/index_home.html'", {"menssage": f"Usuario creado "})
#     else:
#         form = UserCreationForm()
#     return render(request, "home/register.html", {"form": form})



