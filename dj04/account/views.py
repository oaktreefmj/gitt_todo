from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from account.forms import LoginForm

def login(request):
	if request.method == 'GET':
		form=LoginForm()
		return render(request, 'login.html',{'form':form},)
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				request.session['username']=user.username
				return redirect('/index')
			else:
				return redirect('/list')