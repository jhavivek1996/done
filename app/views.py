from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	 login,
	 logout,
	)
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout


def Seller_signup_view(request):
   
    if request.method == 'POST':
        
        form = Seller_form()
        if form.is_valid():
        	form.save()
        	return render(requset, 'signup.html', {'form':form});
   
    else:
        form = Seller_form()
        args= { 'form':form }
        return render(request, 'login.html', {'form':form})
    return HttpResponse("/Thanks Seller")

def Seller_signup_view(request):
   
    if request.method == 'POST':
        
        form = Seller_form()
        if form.is_valid():
        	form.save()
        	return render(requset, 'signup.html', {'form':form});
   
    else:
        form = Seller_form()
        args= { 'form':form }
        return render(request, 'login.html', {'form':form})
    return HttpResponse("/Thanks Seller")

def Library_signup_view(request):
	
   
    if request.method == 'POST':
        
        form = Library_form()
        if form.is_valid():
        	form.save()
        	return render(requset, 'signup.html', {'form':form});
   
    else:
        form = Library_form()
        args= { 'form':form }
        return render(request, 'login.html', {'form':form})
    return HttpResponse("/Thanks Seller")

def User_signup_view(request):
   
    if request.method == 'POST':
        
        form = User_form()
        if form.is_valid():
        	form.save()
        	return render(requset, 'signup.html', {'form':form});
   
    else:
        form = User_form()
        args= { 'form':form }
        return render(request, 'login.html', {'form':form})
    return HttpResponse("/Thanks Seller")
