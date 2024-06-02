from django.shortcuts import render
from rest_framework import generics
from .models import Proffesor
from .serializers import ProffesorSerializer

# Create your views here.

class ProffesorList(generics.ListCreateAPIView):
    queryset = Proffesor.objects.all()
    serializer_class = ProffesorSerializer