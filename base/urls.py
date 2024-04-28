from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.userLogin, name='login'),
	path('servicelogin/', views.serviceLogin, name='servicelogin'),
	path('usersignup/', views.userSignup, name='usersignup'),
	path('servicesignup/', views.serviceSignup, name='servicesignup'),
	path('usereventlist/', views.userEventList, name='usereventlist'),
	path('event/<pk>/', views.event, name='event'),
	path('serviceeventlist/', views.serviceEventList, name='serviceeventlist'),
	path('createevent/', views.createEvent, name='createevent'),
	path('serviceevent/<pk>', views.serviceEvent, name='serviceevent'),
	path('test/', views.test, name='test'),
	path('logout/', views.userLogout, name='logout')
]