from django.urls import path

from .views import ListSponsorAPIView, RetrieveUpdateSponsorAPIView

urlpatterns = [ 
    path('', ListSponsorAPIView.as_view(), name="all-sponsors"),
    path('<int:pk>/', RetrieveUpdateSponsorAPIView.as_view(), name="retrieve-update-sponsor"),
]