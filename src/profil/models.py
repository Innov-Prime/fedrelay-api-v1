from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ProfilModel(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=200)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=200)
    quartier = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)
    avatar = models.CharField(max_length=10000,null=True)

    #==== RELATION ONE TO ONE ENTRE UN USER ET SON PROFIL =====#
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.nom

