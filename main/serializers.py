from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import AuthenticationFailed 

from .models import Donate, Petition_for_legal_entity, Petition_for_physical_entity

from rest_framework_simplejwt.tokens import RefreshToken

from sponsor.models import Sponsor 

class SerializerForLegalEntity(ModelSerializer):

    class Meta:
        model = Petition_for_legal_entity
        fields = ('full_name', 'phone_number', 'amont_of_money', 'organization')


class SerializerForPhysicalEntity(ModelSerializer):

    class Meta:
        model = Petition_for_physical_entity
        fields = ('full_name', 'phone_number', 'amont_of_money')

class LoginSerializer(ModelSerializer):
    username = serializers.CharField(max_length=100) 
    password = serializers.CharField(max_length=100, min_length=6, write_only=True) 
    tokens = serializers.DictField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')  

        user = authenticate(username=username, password=password) 
       
        if not user:
            raise AuthenticationFailed({
                'message': 'Username yoki parol nato`g`ri'
            })
 
        token_refresh = RefreshToken.for_user(user) 

        return {  
            'username': user.username, 
            'tokens': {
                'refresh': str(token_refresh),
                'access': str(token_refresh.access_token)
            }   
        } 
    
class CreateDonateSerializer(ModelSerializer): 
 
    class Meta:
        model = Donate
        fields = ('sponsor_id', 'student_id', 'amont_of_money')

    def validate(self, attrs):
        amont_of_money = attrs.get('amont_of_money', 0) 
        sponsor_id = attrs.get('sponsor_id', '')
        student_id = attrs.get('student_id', '') 

        if sponsor_id.amont_of_money < amont_of_money: 
            raise serializers.ValidationError("Pul yetarli emas")
        
        if amont_of_money + student_id.amont_of_money > student_id.contract:
            raise serializers.ValidationError("Pul kontrakt miqdoridan kam bo`lishi kerak.")
        
        return attrs

        




