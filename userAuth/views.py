from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			print('gaiso login')
			return render(request, "login.html", {'message':'Cannot login'})
	return render(request, 'login.html')

def register_view(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username, email, password)

		if user:
			return redirect('userAuth:login')
	return render(request, 'register.html')

@login_required(login_url="/userAuth/login/")
def logout_view(request):
    logout(request)
    return redirect('index')