from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
	PILIHAN_JURUSAN = [
		('IF', 'INFORMATIKA'),
		('TI', 'TEKNIK INDUSTRI'),
		('TE', 'TEKNIK ELEKTRO'),
		('TM', 'TEKNIK MESIN'),	
		('TK', 'TEKNIK KIMIA')
	]

	nim = models.CharField(max_length=10, unique=True)
	nama = models.CharField(max_length=32)
	jurusan = models.CharField(
		max_length = 2,
		choices = PILIHAN_JURUSAN,
		default = 'IF'
	)

	def __str__(self):
		return f"{self.nim}_{self.nama}"