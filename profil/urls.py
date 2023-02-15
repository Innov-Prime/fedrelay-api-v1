from django.urls import path
from . import views

urlpatterns= [
    # path('profil',views.CreateProfile.as_view(),name='profil'),
    path('<int:user_id>/profil',views.UpdateProfile.as_view(),name="update_avatar")
]