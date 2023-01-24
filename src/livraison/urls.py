from django.urls import path
from . import views

urlpatterns = [
    # ====== USING GENERICS ====== #
    path('<int:pk>/',views.GettingOneDelivery.as_view()),
    path('create/',views.AddingOneDelivery.as_view()),
    path('deliverys/<int:user_id>/',views.GetAllDelivery,name=''),
    path('followUp/',views.FollowUpDelivery)
]