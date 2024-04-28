from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Service, Event
from .forms import LoginForm, SignupForm, ServiceSignupForm, ServiceLoginForm, ServiceCodeForm, CreateEventForm
import random

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		try:
			profile = Profile.objects.get(user=request.user)
			return redirect('usereventlist')
		except:
			return redirect('serviceeventlist')
	return redirect('login')

def userLogin(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				try:
					profile = Profile.objects.get(user=user)
					login(request, user)
					return redirect('usereventlist')
				except ObjectDoesNotExist:
					messages.error(request, 'User is a service (login at service login)')
			else:
				messages.error(request, 'Username OR password is incorrect')

	context = {'form': LoginForm}
	return render(request, 'login.html', context)

def serviceLogin(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = ServiceLoginForm(request.POST)

		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				try:
					service = Service.objects.get(user=user)
					login(request, user)
					return redirect('serviceeventlist')
				except ObjectDoesNotExist:
					messages.error(request, 'User is not a service (login at user login)')
			else:
				messages.error(request, 'Company name OR password is incorrect')

	context = {'form': ServiceLoginForm}
	return render(request, 'servicelogin.html', context)

def userSignup(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			if password1 != password2:
				messages.error(request, 'Passwords do not match')
			else:
				User.objects.create_user(username=username, password=password1)
				user = User.objects.get(username=username)
				userId = user.id
				profile = Profile(user=user)
				profile.save()

				user = authenticate(request, username=username, password=password1)
				login(request, user)
				return redirect('usereventlist')
	context = {'form': SignupForm}
	return render(request, 'usersignup.html', context)

def serviceSignup(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = ServiceSignupForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			address = request.POST.get('address')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			if password1 != password2:
				messages.error(request, 'Passwords do not match')
			else:
				User.objects.create_user(username=username, password=password1)
				user = User.objects.get(username=username)
				userId = user.id
				profile = Service(user=user, address=address)
				profile.save()

				user = authenticate(request, username=username, password=password1)
				login(request, user)
				return redirect('serviceeventlist')
	context = {'form': ServiceSignupForm}
	return render(request, 'servicesignup.html', context)

def userEventList(request):
	q = Service.objects.all()
	context = {"service_list": q}
	return render(request, 'usereventlist.html', context)

def event(request, pk):
	q = Service.objects.get(id=pk)
	try:
		e = q.event.all().order_by('-id')[0]
		profile = Profile.objects.get(user=request.user)
		for user in e.user.all():
			if user == profile:
				e = False
				break

		if request.method == 'POST':
			form = ServiceCodeForm(request.POST)
			if form.is_valid():
				if int(request.POST.get('code')) != int(e.code):
					messages.error(request, 'Invalid Code')
				else:
					u = Profile.objects.get(user=request.user)
					e.user.add(u)
					e.amount -= 1
					e.save()
					return redirect('usereventlist')
	except IndexError:
		e = None

	context = {"service": q, "event": e, "form": ServiceCodeForm}
	return render(request, 'service.html', context)

def serviceEventList(request):
	service = Service.objects.get(user=request.user)
	q = Event.objects.filter(service=service).order_by('-id')
	context = {"event_list": q}
	return render(request, 'serviceeventlist.html', context)

def createEvent(request):
	if request.method == 'POST':
		form = CreateEventForm(request.POST)
		if form.is_valid():
			item = request.POST.get('item')
			amount = request.POST.get('amount')
			category = request.POST.get('category')
			start_time = request.POST.get('start_time')
			end_time = request.POST.get('end_time')
			code = random.randint(100000, 999999)

			event = Event(items=item,amount=amount,category=category,start_time=start_time,end_time=end_time,code=code)
			event.save()
			service = Service.objects.get(user=request.user)
			service.event.add(event)
			service.save()
			return redirect('serviceeventlist')
	context = {'form': CreateEventForm}
	return render(request, 'createevent.html', context)

def serviceEvent(request, pk):
	q = Event.objects.get(id=pk)
	context = {"event": q}
	return render(request, 'event.html', context)

def test(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request, 'test.html')

def userLogout(request):
	logout(request)
	return redirect('login')