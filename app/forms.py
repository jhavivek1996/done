from django import forms
from .models import *
from django.forms import ModelForm


class Seller_form(forms.ModelForm):

    class Meta:
        model = Seller_registration
        fields = '__all__'

class Library_form(forms.ModelForm):

    class Meta:
        model = Library_registration
        fields = '__all__'

class User_form(forms.ModelForm):

    class Meta:
        model = User_registration
        fields = '__all__'