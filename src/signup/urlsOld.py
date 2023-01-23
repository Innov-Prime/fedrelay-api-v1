from django.urls import path

from . import views

urlpatterns= [
    path('create/',views.UserRegister.as_view(),name=''),
    path('login/',views.Login,name='')
]