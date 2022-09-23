from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
	path('', views.index, name='index'),
	path('men/', views.men, name='men'),
	path('women/', views.women, name='women'),
	path('about/', views.about, name='about'),
	path('contact/', views.women, name='women'),
]