from django.urls import path

from .views import (
    CreatePetitionForLegalAPIView, 
    CreatePetitionForPhysicalAPIView, 
    LoginAPIView,
    CreateDonateAPIView,
    Dashboard
)

urlpatterns = [
    path('create-petition-for-legal/', CreatePetitionForLegalAPIView.as_view(), name='create-petition-for-legal'),
    path('create-petition-for-physical/', CreatePetitionForPhysicalAPIView.as_view(), name='create-petition-for-physical'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('create-donate/', CreateDonateAPIView.as_view(), name='create-donate'),
    path('', Dashboard.as_view(), name='dashboard'),
    
]