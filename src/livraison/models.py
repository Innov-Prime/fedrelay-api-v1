from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Delivery(models.Model):
    
    # ====  PREMIER FORMULAIRE =======#
    nomEmetteur = models.CharField(max_length=100)
    prenomEmetteur = models.CharField(max_length=100)
    telephoneEmetteur = models.CharField(max_length=100)
    lieuColis = models.CharField(max_length = 200)
    detailLocalisation = models.TextField(max_length=500)

    # ====  DEUXIEME FORMULAIRE =======#
    villeReception = models.CharField(max_length = 200)
    pointRelais = models.CharField(max_length = 200)
    notification = models.TextField(max_length = 500)

    # ====  TROIXIEME FORMULAIRE =======#
    nomDestinataire = models.CharField(max_length = 200)
    prenomDestinataire = models.CharField(max_length = 200)
    telephoneDestinataire = models.CharField(max_length = 200)
    emailDestinataire = models.EmailField()

    # ====  QUATRIEME FORMULAIRE ==== #
    typeColis = models.CharField(max_length = 200)
    poids = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)

    follow_code = models.CharField(max_length = 200,null=True)
    status = models.CharField(max_length = 200,default="En cours")
    client_id = models.IntegerField()

    ##================= RELATION ENTRE LE USER ET LA LIVRAISON =============##

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomEmetteur