from django.db import models

# Create your models here.
class Login(models.Model):
	fullname = models.CharField(max_length=120,blank=False)
	password = models.CharField(max_length=120,blank=False)

class Converter1(models.Model):
	status=(('INR',"INR"),
		("USD","USD"),
		("EUR","EUR"),
		("GBP","GBP"),
		("SGB","SGB"))
	convertfrom = models.CharField(
		choices=status,
		max_length=3,
		blank = False,
		default='INR',

	)
	convertto = models.CharField(
		choices=status,
		max_length=3,
		default='USD',
    	blank = False,
    	)
	amount = models.IntegerField(blank= False)