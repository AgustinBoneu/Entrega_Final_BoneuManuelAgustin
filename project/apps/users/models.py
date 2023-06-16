from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    celular = models.CharField(max_length=20,blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars',blank=True, null=True)
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
    def __str__(self):
        return f"{self.usuario.username}"