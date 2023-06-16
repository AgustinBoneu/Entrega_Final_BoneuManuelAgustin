from django.views.generic import  TemplateView

# Create your views here.

class IndexViews(TemplateView):
    template_name = "users/user.html"
