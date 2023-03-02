from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView 

from .serializers import SponsorListSerializer, RetrieveSponsorSerializer, UpdateSponsorSerializer
from .models import Sponsor

class ListSponsorAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer
    filterset_fields = ['status', 'amont_of_money']
    

class RetrieveUpdateSponsorAPIView(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()

    def get_serializer_class(self): 
        if self.request.method == 'GET': 
            return RetrieveSponsorSerializer 
        elif self.request.method == 'PUT' or 'PATCH': 
            return UpdateSponsorSerializer
