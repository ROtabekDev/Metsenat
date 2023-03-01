from django.utils import timezone
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Sum

from student.models import Student

from .serializers import (
    SerializerForLegalEntity, 
    SerializerForPhysicalEntity, 
    LoginSerializer,
    CreateDonateSerializer
)

class CreatePetitionForLegalAPIView(CreateAPIView):
    serializer_class = SerializerForLegalEntity
    permission_classes = [AllowAny]

class CreatePetitionForPhysicalAPIView(CreateAPIView):
    serializer_class = SerializerForPhysicalEntity
    permission_classes = [AllowAny]

class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        pass

class CreateDonateAPIView(CreateAPIView):
    serializer_class = CreateDonateSerializer

class Dashboard(APIView): 

    def get(self, request, *args, **kwargs):
        
        amont_of_money_sum = Student.objects.aggregate(Sum('amont_of_money'))['amont_of_money__sum']
        contract_sum = Student.objects.aggregate(Sum('contract'))['contract__sum']
        other = contract_sum - amont_of_money_sum

        data = {
            'Jami to`langan summa:': amont_of_money_sum,
            'Jami so`ralgan summa:': contract_sum,
            'To`lanishi kerak bo`lgan summa:': other
        }
 
        return Response(data=data)
