from django import forms

from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
	class Meta:
		model = Mahasiswa
		fields = "__all__"