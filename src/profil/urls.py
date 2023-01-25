from django.urls import path
from . import views

urlpatterns= [
    path('<str:user_token>/profil',views.CreateProfile.as_view(),name='profil'),
    path('<int:user_id>/<str:user_token>/avatar',views.UpdateAvatar.as_view(),name="update_avatar")
]