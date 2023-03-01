 
from rest_framework import serializers

from .models import Student, University
from main.models import Donate
from main.serializers import CreateDonateSerializer

class CreateUniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ('name',)

class ListStudentSerializer(serializers.ModelSerializer):
    university_id = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ('full_name', 'degree', 'university_id', 'contract', 'amont_of_money')

class CreateStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university_id', 'degree', 'contract')


class RetrieveStudentSerializer(serializers.ModelSerializer):
    university_id = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university_id', 'degree', 'contract', 'amont_of_money')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        donates = Donate.objects.filter(student_id=instance) 
        
        serializer = CreateDonateSerializer(donates,  many=True)
         
        representation['donates'] = serializer.data
        return representation
    
class UpdateStudentSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university_id', 'degree', 'contract', 'amont_of_money')