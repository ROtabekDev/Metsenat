from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

from .models import Student, University
from .serializers import (
    CreateUniversitySerializer, 
    ListStudentSerializer, 
    CreateStudentSerializer,
    RetrieveStudentSerializer,
    UpdateStudentSerializer
)

class CreateUniversityAPIView(CreateAPIView):
    serializer_class = CreateUniversitySerializer

class ListStudentAPIView(ListAPIView):
    serializer_class = ListStudentSerializer
    queryset = Student.objects.all()
    filterset_fields = ['degree', 'university_id']
     
class CreateStudentAPIView(CreateAPIView):
    serializer_class = CreateStudentSerializer

class RetrieveStudentAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = RetrieveStudentSerializer
    
class UpdateStudentAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer