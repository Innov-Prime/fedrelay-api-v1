from rest_framework import serializers
from .models import Relaypoint

class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relaypoint
        fields = ["title","description","status","localisation","map_address"]