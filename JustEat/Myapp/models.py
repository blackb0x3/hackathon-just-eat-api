from django.db import models
from django.conf import settings
from django.utils import timezone

class Users(models.Model):
	name = models.CharField(max_length = 40, null = False)
	email = models. models.CharField(null = False)
	contact_number = models.CharField(max_digits = 15, null = False)
	picture = models.ImageField(upload_to = 'users/users_img', blank = True)
	password = models.CharField(min_length = 6, max_length = 20, null = False)
    	address = models.CharField(max_length = 250, null = False)
    	city = models.CharField(max_length = 30, null = False)
    	postcode = models.CharField(max_length = 30, null = False)
	terms_conditions = models.BooleanField(default = False, null = False)
	validation = models.BooleanField(default = False, null = False)
	company = models.BooleanField(default = False, null = False)

class Allergies(model.Model):
	ingredient = models.CharField(max_length = 30)

class Requests(model.Model):
	food = models.CharField(max_length = 50)
	picture = models.ImageField(upload_to = 'food/food_img', blank = True)
	comment = models. models.TextField(blank = True, null = False)
	tempreture = models.BooleanField(blank = False)
	time = models.TimeField(default=timezone.now)
	name = models.ForeignKey(Users)
	contact_number = models.ForeignKey(Users)
	address = models.ForeignKey(Users)
	city = models.ForeignKey(Users)
	postcode = models.ForeignKey(Users)
	ingredient = models.ForeignKey(Allergies)



 
