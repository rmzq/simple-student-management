from rest_framework import viewsets
from .serializers import MahasiswaSerializer
from management.models import Mahasiswa

class MahasiswaViewSet(viewsets.ModelViewSet):
	queryset = Mahasiswa.objects.all()
	serializer_class = MahasiswaSerializer