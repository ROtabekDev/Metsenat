from rest_framework.serializers import ModelSerializer

from .models import Sponsor

class SponsorListSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        fields = (
                  'id',
                  'full_name', 
                  'phone_number', 
                  'amont_of_money', 
                  'spent_money', 
                  'created_at', 
                  'status'
                  )
        
class RetrieveSponsorSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'amont_of_money', 'organization')

class UpdateSponsorSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'status', 'amont_of_money', 'payment_type', 'organization')