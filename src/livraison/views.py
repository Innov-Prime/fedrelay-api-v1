from django.shortcuts import render
from django.http import JsonResponse

from django.forms.models import model_to_dict 
from .models import Delivery

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DeliverySerializer

from rest_framework import generics,status

from datetime import datetime
from .utils import sendEmailBox

import random

# Create your views here.

@api_view(['GET'])
def GetAllDelivery(request,user_id):
    query = Delivery.objects.filter(user_id=user_id).order_by('-id')
    serialization = DeliverySerializer(query,many=True)
    return Response(serialization.data)


class GettingOneDelivery(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class AddingOneDelivery(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)



    def perform_create(self, serializer):
        #======= ENVOIE DE MAIL AU RECEIVER ======#
        client_id = serializer.validated_data.get('client_id')
        sender_name = serializer.validated_data.get('nomEmetteur')
        sender_lastname = serializer.validated_data.get('prenomEmetteur')

        colis_receiver_email = serializer.validated_data.get('emailDestinataire')
        colis_recever_name = serializer.validated_data.get('nomDestinataire')
        name = serializer.validated_data.get('nomEmetteur')

        subject = "Livraison sur FedRelay"
        template = 'livraison_email.html'

        #### FORMATION DU CODE DE SUIVI ####
        list = ["A","B","C","D","E","F","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letter_rand = random.choice(list)
        rand = random.randint(0,10000)

        print(client_id)

        # now = datetime.now()
        # timestamp = datetime.timestamp(now)
        # follow_code = "##"+str(timestamp) +"##" ### CODE DE SUIVI
        follow_code = "R"+str(client_id)+str(rand)+letter_rand ### CODE DE SUIVI
        print(follow_code)

        serializer.validated_data['follow_code']=follow_code

        context = {
            'name':name,
            'date':datetime.today().date,
            'colis_recever_name':colis_recever_name,
            'follow_code':follow_code,
            'sender_name':sender_name,
            'sender_lastname':sender_lastname
        }
        
        receivers = [colis_receiver_email]

        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            serializer.save()
            print('envoyé avec succes!!')
        else:
            print('echoué avec succes!!')
        
        


##================   =============##

# #SUIVI D'UNE LIVRAISON
# class FollowUpDelivery(generics.RetrieveAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer
#     lookup_field = 'follow_code'


### SUIVI D'UNE LIVRAISON
@api_view(['POST'])
def FollowUpDelivery(request):
    data = dict(request.data)
    code_sent = data['follow_code']
    query =  Delivery.objects.filter(follow_code=code_sent)
    serialization = DeliverySerializer(query,many=True)

    print(code_sent)
    print(serialization.data)

    if query:
        # QUAND LA LIVRAISON EXISTE 
        return Response(
            {
                'success':True,
                'command_status':serialization.data[0]['status']
            })
    else:
        # QUAND LA LIVRAISON N'EXISTE PAS
        return Response({'success':False})
