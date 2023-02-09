from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from .utils import sendEmailBox
from rest_framework.response import Response

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User

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

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        email = request.data['username']

        subject = "Connexion sur FedRelay"
        template = 'login.html'
        context = {
            'email':email,
        }
        receivers = [email]
        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            print('envoyé avec succes!!')
        else:
            print("L'envoie de mail a échoué!!")


        # return super(LoginAPI, self).post(request, format=None)

        return Response({
                "user": UserSerializer(user).data,
                "token": AuthToken.objects.create(user)[1]
            })