from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mahasiswa
from .forms import MahasiswaForm
# Create your views here.

# def index(request, nm):
# 	return render(request, 'management/index.html',{
# 		'name' : nm.capitalize()
# 	})

def show(request):
	mahasiswa = Mahasiswa.objects.all()
	return render(request, 'management/show.html', {'mahasiswa':mahasiswa})

def create(request):
	if request.method == "POST":
		form = MahasiswaForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/management')
			except:
				pass
	else:
		form = MahasiswaForm()
	return render(request,'management/create.html',{'form':form})

def edit(request, id):
	mahasiswa = Mahasiswa.objects.get(id=id)
	return render(request, 'management/edit.html', {'mahasiswa':mahasiswa})

def update(request, id):
	mahasiswa = Mahasiswa.objects.get(id=id)
	form = MahasiswaForm(request.POST, instance = mahasiswa)
	if form.is_valid():
		form.save()
		return redirect('/management')
	return render(request, 'management/edit.html', {'mahasiswa':mahasiswa})

def delete(request, id):
	mahasiswa = Mahasiswa.objects.get(id=id)
	mahasiswa.delete()
	return redirect('/management')