from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from .serializer import ProfilSerializer
from .models import ProfilModel
from rest_framework.response import Response

# Create your views here.

class CreateProfile(generics.CreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data,status=status.HTTP_201_CREATED,headers=headers)

class UpdateAvatar(generics.UpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'

    
