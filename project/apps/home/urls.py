from django.conf import settings
from os import stat
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexhome, name="index home"),
    path("about/", views.abouthome, name="about"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
