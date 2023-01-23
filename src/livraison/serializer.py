from rest_framework import serializers
from .models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = (
        "id",
        "user",
        "client_id",
        "nomEmetteur",
        "prenomEmetteur",
        "telephoneEmetteur",
        "lieuColis",
        "detailLocalisation",

        "villeReception",
        "pointRelais",
        "notification",

        "nomDestinataire",
        "prenomDestinataire",
        "telephoneDestinataire",
        "emailDestinataire",

        "typeColis",
        "poids",
        "description",
        "status",
        "follow_code")