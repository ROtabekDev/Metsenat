from django.urls import path

from .views import (
    CreateUniversityAPIView, 
    ListStudentAPIView, 
    CreateStudentAPIView,
    RetrieveStudentAPIView,
    UpdateStudentAPIView
)

urlpatterns = [ 
        path('', ListStudentAPIView.as_view(), name='all-students'),
        path('<int:pk>/', RetrieveStudentAPIView.as_view(), name='all-students'),
        path('update/<int:pk>/', UpdateStudentAPIView.as_view(), name='all-students'),
        path('create/', CreateStudentAPIView.as_view(), name='create-student'),
        path('create-university/', CreateUniversityAPIView.as_view(), name='create-university'),
    ]