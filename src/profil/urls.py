from django.urls import path
from . import views

urlpatterns= [
    path('profil/',views.CreateProfile.as_view(),name='profil'),
    path('avatar/<int:user_id>/',views.UpdateAvatar.as_view(),name="update_avatar")
]