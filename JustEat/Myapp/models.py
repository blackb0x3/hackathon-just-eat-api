from django.db import models
from django.conf import settings
from django.utils import timezone

class Users(models.Model):
	name = models.CharField(max_length = 40, null = False)
	email = models.CharField(null = False)
	contact_number = models.CharField(max_length = 15, null = False)
	picture = models.ImageField(upload_to = 'images/users_img', blank = True)
	contact_number = models.CharField(max_length = 15, null = False)
	picture = models.ImageField(upload_to = 'images/users_img', blank = True)
	password = models.CharField(min_length = 6, max_length = 20, null = False)
	address = models.CharField(max_length = 250, null = False)
	city = models.CharField(max_length = 30, null = False)
	postcode = models.CharField(max_length = 30, null = False)
	terms_conditions = models.BooleanField(default = False, null = False)
	validation = models.BooleanField(default = False, null = False)
	company = models.BooleanField(default = False, null = False)

class Allergies(models.Model):
	ingredient = models.CharField(max_length = 30)

class Requests(models.Model):
	food = models.CharField(max_length = 50)
	picture = models.ImageField(upload_to = 'images/food_img', blank = True)
	comment = models.TextField(blank = True, null = False)
	tempreture = models.BooleanField(blank = False)
	time = models.TimeField(default=timezone.now)
	name = models.ForeignKey(Users,on_delete=models.CASCADE)
	contact_number = models.ForeignKey(Users,on_delete=models.CASCADE)
	address = models.ForeignKey(Users,on_delete=models.CASCADE)
	city = models.ForeignKey(Users,on_delete=models.CASCADE)
	postcode = models.ForeignKey(Users,on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Allergies,on_delete=models.CASCADE)



 
