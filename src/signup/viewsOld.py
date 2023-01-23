from django.http import HttpResponse

from rest_framework.response import Response
# from django.contrib.auth.models import User

from .modelsOld import UserFedrelay

from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework import generics

from django.forms.models import model_to_dict

from datetime import datetime
from .utils import sendEmailBox
from rest_framework.response import Response


# Create your views here.

class UserRegister(generics.CreateAPIView):
    queryset = UserFedrelay.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        #======= ENVOIE DE MAIL AU RECEIVER ======#
        email = serializer.validated_data.get('email')

        subject = "Inscription sur FedRelay"
        template = 'signup_email.html'
        context = {
            'email':email,
        }
        receivers = [email]

        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            serializer.save()
            print('envoyé avec succes!!')
        else:
            print('echoué avec succes!!')
            return Response({'error':"L'envoie de mail a échoué!!"})


@api_view(['POST'])
def Login(request):
    data = request.data
    data = dict(data)

    password = data['password']
    email = data['email']
    phone = data['phone']

    if not email:
        user = UserFedrelay.objects.filter(email=email,)
    else:
        user = UserFedrelay.objects.filter(phone=phone,)


    if not user:
        error = {'error':'Connexion échouée! Veuillez revoir vos coordonnées!' }
        return Response(error)
    else:
        user = UserFedrelay.objects.get(password=password)
        user.is_active = True

        user.save()

        auth_user = {
                        'password':data['password'],
                        'email': data['email']
                    }
        return Response(auth_user)
