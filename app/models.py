from django.db import models

class Seller_registration(models.Model):
	Id=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=255)
	Contact_no=models.IntegerField()
	Email=models.EmailField(max_length=30)
	Website=models.CharField(max_length=255)

class Library_registration(models.Model):
	Id=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=255)
	Contact_no=models.IntegerField()
	Email=models.EmailField(max_length=30)
	Website=models.CharField(max_length=255)
	Symbol=models.ImageField(upload_to='img/')
	Date_of_establishment=models.DateTimeField()
	Policy=models.CharField(max_length=255)
	Membership_Details=models.CharField(max_length=255)

class User_registration(models.Model):
	Id=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=255)
	Contact_no=models.IntegerField()
	Email=models.EmailField(max_length=30)
	Website=models.CharField(max_length=255)