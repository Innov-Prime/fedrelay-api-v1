from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyUser 

from .utils import sendEmailBox
from rest_framework.response import Response

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','phone')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #### ==== ENREGISTREMENT DU USER ===== ####
        user = MyUser.objects.create_user(validated_data['username'], validated_data['email'],validated_data['phone'], validated_data['password'])

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        email = validated_data['email']

        subject = "Inscription sur FedRelay"
        template = 'signup_email.html'
        context = {
            'email':email,
        }
        receivers = [email]
        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            print('envoyé avec succes!!')
        else:
            print("L'envoie de mail a échoué!!")
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = MyUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)