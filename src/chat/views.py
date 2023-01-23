from django.shortcuts import render

from rest_framework import generics
from .models import Chat
from .serializer import ChatSerializer

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ClientMessageCreate(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


