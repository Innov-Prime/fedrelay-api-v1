from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from .serializer import ProfilSerializer
from .models import ProfilModel
from rest_framework.response import Response

from knox.models import AuthToken

# Create your views here.


class CreateProfile(generics.CreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

    def create(self, request,*args, **kwargs):
        ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

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

        if is_user_authenticated:    
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'success':True}
            # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response(data,status=status.HTTP_201_CREATED,headers=headers)
        else:
            return Response({"success":False, "detail":"Veuillez vous authentifier"})

class UpdateAvatar(generics.UpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'

    def update(self, request, *args, **kwargs):

        ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##
        
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

        if is_user_authenticated: 
            #Update de l'avatar si le user est authyentifié
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response({"success":False, "detail":"Veuillez vous authentifier"})


        

