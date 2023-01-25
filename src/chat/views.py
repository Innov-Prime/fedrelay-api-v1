from django.shortcuts import render

from rest_framework import generics
from .models import Chat
from .serializer import ChatSerializer

from rest_framework.response import Response
from rest_framework import status

from knox.models import AuthToken

# Create your views here.

#MY AUTHENTICATION FUNCTION
def Chat_Authentication(request,kwargs):
    ## MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

    #Récupération du token envoyé par le client
    token_sent = kwargs['user_token']
    
    user_id = request.data['user']

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



class ClientMessageCreate(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        ### VERIFIONS SI LE USER EST CONNECTEE OU PAS ###

        if Chat_Authentication(request,kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'success':True}
            # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"success":False, "detail":"Veuillez vous authentifier"})


class GetAllClientMessage(generics.ListAPIView):
    queryset = Chat.objects.all().order_by('-id')
    serializer_class = ChatSerializer
    lookup_field = 'user_id'

    def list(self, request, *args, **kwargs):

        ## MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

        #Récupération du token envoyé par le client
        token_sent = kwargs['user_token']
        user_id = kwargs['user_id']

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
        if is_user_authenticated:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"success":False, "detail":"Veuillez vous authentifier"})