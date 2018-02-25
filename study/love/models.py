from django.db import models

# Create your models here.
class Login(models.Model):
	fullname = models.CharField(max_length=120,blank=False)
	password = models.CharField(max_length=120,blank=False)
