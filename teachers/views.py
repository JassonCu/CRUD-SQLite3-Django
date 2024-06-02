from rest_framework import viewsets
from .models import Proffesor
from .serializers import ProffesorSerializer

# Create your views here.

class ProffesorViewsSet(viewsets.ModelViewSet):
    queryset = Proffesor.objects.all()
    serializer_class = ProffesorSerializer