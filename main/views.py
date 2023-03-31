from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Claim

# Create your views here.

def home(request):

	if request.user.username == 'admin':
		claim_all = Claim.objects.all()
	else:
		claim_all = Claim.objects.filter(Q(user=request.user.username) | Q(assigned=request.user.username))

	_len = len(claim_all)
	data = {'claims': claim_all, 'len': _len}

	return render(request, 'index.html', context=data)

def claim(request):
	if request.method == 'POST':
		topic = request.POST.get('topic')
		text = request.POST.get('discription')
		_class = request.POST.get('class')
		status = 0

		claim = Claim(topic=topic,
					  text=text,
					  cabinet=_class,
					  status=status,
					  user=request.user.username,
					  lastname=request.user.last_name,
					  firstname=request.user.first_name,
					  assigned='',
					  assigned_firstname='',
					  assigned_lastname='')
		claim.save()
		return redirect('/')
	else:
		return render(request, 'claim.html')

def showclaim(request, id):
	if request.method == 'POST':
		success = request.POST.get('success')
		assigned = request.POST.get('assigned')
		if assigned:
			assigned_user = User.objects.get(username=assigned)
			Claim.objects.filter(id=id).update(assigned=assigned_user.username,
											   assigned_firstname=assigned_user.first_name,
											   assigned_lastname=assigned_user.last_name,
											   status=1)
			return redirect('/')
		if success:
			Claim.objects.filter(id=id).update(assigned='',
											   assigned_firstname='',
											   assigned_lastname='',
											   status=2)
			return redirect('/')
	claim = Claim.objects.get(id=id)
	assigneds = User.objects.all()
	data = {'id': id,
			'claim': claim,
			'firstname': claim.firstname,
			'lastname': claim.lastname,
			'assigneds': assigneds}
	return render(request, 'showclaim.html', context=data)