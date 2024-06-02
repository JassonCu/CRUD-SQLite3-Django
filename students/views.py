from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Students

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer