from django.urls import path
from . import views

urlpatterns = [
    path("<user_token>/client", views.ClientMessageCreate.as_view(),name='client_chat'),
    path("<user_id>/<user_token>/client",views.GetAllClientMessage.as_view(),name="getmsg")
]