from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def auth(request):
	if request.method == 'POST':
		username = request.POST['login']
		password = request.POST['pass']
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return HttpResponse('Invalid login...')
	else:
		return render(request, 'login.html')

def log_out(request):
	logout(request)
	return redirect('/')