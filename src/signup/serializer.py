
from rest_framework import serializers

from .modelsOld import UserFedrelay

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFedrelay
        fields = ["email","phone","password","is_active"]
