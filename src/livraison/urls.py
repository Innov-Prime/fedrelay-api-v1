from django.urls import path
from . import views

urlpatterns = [
    # ====== USING GENERICS ====== #
    path('<str:user_token>/create',views.AddingOneDelivery.as_view()),
    path('<user_id>/<str:user_token>/deliveries',views.GetAllDelivery,name=''),
    path('<int:user_id>/<str:user_token>/followup',views.FollowUpDelivery)
]