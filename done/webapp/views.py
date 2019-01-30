from django.shortcuts import render,redirect,HttpResponse

from django.contrib import messages
from .forms import *
from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth import PasswordChangeForm

def home(request):
	return render(request, 'users/home.html')

def loggedin(request):
    return render(request, 'users/loggedin.html')

def sellerregister(request):
	if request.method=="POST":
		form= SellerRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('A New user has  been created'))
			#return redirect('login')
			
	else:
		form= SellerRegisterForm()
	return render(request, 'users/sellerregister.html', {'form':form })

def libraryregister(request):
    if request.method=="POST":
        form= LibraryRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('A New user has  been created'))
            #return redirect('login')
            
    else:
        form= LibraryRegisterForm()
    return render(request, 'users/libraryregister.html', {'form':form })

def userregister(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('A New user has  been created'))
            #return redirect('login')
            
    else:
        form= UserRegisterForm()
    return render(request, 'users/userregister.html', {'form':form })

#function property alias name change manually

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST,instance='__all__')
        if form.is_valid():
        	form.save()
        	return redirect('/account/profile')
    else:
        form = PasswordChangeForm()

        args={'form':form}
        return render(request, 'users/change_password.html',{'form' :form})
'''
    if request.method=='GET':
    	return render(request, 'users/change_password.html')


    	
'''


