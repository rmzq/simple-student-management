from rest_framework import serializers

from management.models import Mahasiswa

class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mahasiswa
		fields = ('id', 'nim', 'nama', 'jurusan')