from django.shortcuts import render,redirect

#auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from utils.forms import UserCreationForm,UserLoginForm

from django.http import HttpResponse
def Signup(request,*args,**kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'accounts/signup.html',{'form':form})
@login_required(login_url='/login/')
def Home(request):
	return render(request,'home/home.html',{})

def Login(request,*args,**kwargs):
	if request.user.is_authenticated:
		return redirect('home')
	form = UserLoginForm(request.POST or None)
	print(form)
	if form.is_valid():
		user_obj=form.cleaned_data.get('user_obj')
		login(request, user_obj)
		return redirect('home')
	return render(request, "accounts/login.html",{'form':form,})
def Logout(request):
	logout(request)
	return redirect('login')