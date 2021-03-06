from django.urls import path
from . import views

urlpatterns = [
	path('', views.show, name='show'),
	path('create', views.create, name='create'),
	path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]