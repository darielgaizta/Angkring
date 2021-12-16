from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('<str:angkringan>/', views.angkringan, name='angkringan'),
	path('checkview', views.checkview, name='checkview'),
	path('send', views.send, name='send'),
	path('getMessages/<str:angkringan>/', views.getMessages, name='getMessages'),
]