from django.shortcuts import  render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse


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


