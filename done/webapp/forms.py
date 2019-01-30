from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SellerRegisterForm(UserCreationForm):
	Id=forms.IntegerField()
	Name=forms.CharField()
	Address=forms.CharField()
	Contact_no=forms.IntegerField()
	Website=forms.CharField()

	class Meta:
		model = User
		fields =['username','email','password1','password2',]

class LibraryRegisterForm(UserCreationForm):
	Id=forms.IntegerField()
	Name=forms.CharField()
	Address=forms.CharField()
	Contact_no=forms.IntegerField()
	Website=forms.CharField()
	#Symbol
	Date_of_establishment=forms.CharField()
	Time=forms.CharField()
	Membership_details=forms.CharField()



	class Meta:
		model = User
		fields =['username','email','password1','password2',]

class UserRegisterForm(UserCreationForm):
	Id=forms.IntegerField()
	Name=forms.CharField()
	Address=forms.CharField()
	Contact_no=forms.IntegerField()
	

	class Meta:
		model = User
		fields =['username','email','password1','password2',]

