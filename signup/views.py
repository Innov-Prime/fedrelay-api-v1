from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from .utils import sendEmailBox
from rest_framework.response import Response

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User

# Register API

#================= CREATION DE PROFIL DU USER PENDANT SON ENREGISTREMENT  ==========#
from rest_framework import status
from profil.serializer import ProfilSerializer
from profil.models import ProfilModel
from django.forms.models import model_to_dict

class CreateProfile(generics.CreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

    def create(self, request,user,*args, **kwargs):
        profil = ProfilModel.objects.create(user=user,nom='',prenom='',telephone=request.data['phone'],email=request.data['email'],profession='',pays='',ville='',quartier='',avatar='')
        return model_to_dict(profil)

class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        userProfil = CreateProfile.create(self, request,user,*args, **kwargs)

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        email = request.data.get('email')

        subject = " Inscription sur FedRelay"
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

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "userProfil": userProfil
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
  
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # print(request.data['username'])
        
        login(request, user)

        profil = ProfilModel.objects.get(user=user)
        userProfile =  model_to_dict(profil)

        return Response({
                "user": UserSerializer(user).data,
                "token": AuthToken.objects.create(user)[1],
                "userProfile":userProfile
            })