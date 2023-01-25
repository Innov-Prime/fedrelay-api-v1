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

from knox.models import AuthToken
# Create your views here.

def Post_Delivry_Authentication(request,kwargs):
    ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

    #Récupération du token envoyé par le client
    token_sent = kwargs['user_token']
    user_id = request.data['user']

    # print(user_id)
    
    #Recuperation des 8 premiers caractères du token envoyé par le client
    one = token_sent[0]
    two = token_sent[1]
    tree = token_sent[2]
    four = token_sent[3]
    five = token_sent[4]
    six = token_sent[5]
    seven = token_sent[6]
    eight = token_sent[7]
    
    #Formation du token de 8 caractères suivant le format qui se trouve dans la DB
    user_token_formed = one+two+tree+four+five+six+seven+eight

    #Verification de l'existance de ce token dans la DB
    is_user_authenticated = AuthToken.objects.filter(token_key=user_token_formed,user_id=user_id)

    #Action après vérification
    return is_user_authenticated

def Get_Delivry_Authentication(kwargs):
    ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

    #Récupération du token envoyé par le client
    token_sent = kwargs['user_token']
    user_id = kwargs['user_id']

    # print(user_id)
    
    #Recuperation des 8 premiers caractères du token envoyé par le client
    one = token_sent[0]
    two = token_sent[1]
    tree = token_sent[2]
    four = token_sent[3]
    five = token_sent[4]
    six = token_sent[5]
    seven = token_sent[6]
    eight = token_sent[7]
    
    #Formation du token de 8 caractères suivant le format qui se trouve dans la DB
    user_token_formed = one+two+tree+four+five+six+seven+eight

    #Verification de l'existance de ce token dans la DB
    is_user_authenticated = AuthToken.objects.filter(token_key=user_token_formed,user_id=user_id)

    #Action après vérification
    return is_user_authenticated

@api_view(['GET'])
def GetAllDelivery(request,*args, **kwargs):
    #VERIFIONS SI LE USER EST AUTHENTIFIE OU PAS
    if Get_Delivry_Authentication(kwargs):
        query = Delivery.objects.filter(user_id=kwargs['user_id']).order_by('-id')
        serialization = DeliverySerializer(query,many=True)
        return Response(serialization.data)
    else:
        return Response({"success":False, "detail":"Veuillez vous authentifier"})

class AddingOneDelivery(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def create(self, request, *args, **kwargs):

        #VERIFIONS SI LE USER EST AUTHENTIFIE OU PAS
        if Post_Delivry_Authentication(request,kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'success':True}
            # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"success":False, "detail":"Veuillez vous authentifier"})



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
        

### SUIVI D'UNE LIVRAISON
@api_view(['POST'])
def FollowUpDelivery(request, *args, **kwargs):

    #VERIFIONS SI LE USER EST AUTHENTIFIE OU PAS
    if Get_Delivry_Authentication(kwargs):
        data = dict(request.data)
        code_sent = data['follow_code']
        query =  Delivery.objects.filter(follow_code=code_sent)
        serialization = DeliverySerializer(query,many=True)

        if query:
            # QUAND LA LIVRAISON EXISTE 
            return Response(
                {
                    'success':True,
                    'command_status':serialization.data[0]['status']
                })
        else:
            # QUAND LA LIVRAISON N'EXISTE PAS
            return Response({'success':False,"detail":"Cette livraison n'existe pas!"})
    
    return Response({"success":False, "detail":"Veuillez vous authentifier"})
    
