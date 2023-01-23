from django.urls import path
from . import views

urlpatterns = [
    path("client/", views.ClientMessageCreate.as_view(),name='client_chat'),
]