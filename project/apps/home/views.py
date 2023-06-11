from django.shortcuts import  render


# Create your views here.
def indexhome (request):
    return render(request, 'home/index_home.html')  

