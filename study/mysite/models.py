from django.db import models

# Create your models here.
class Leaderboard(models.Model):
	name = models.CharField(max_length=120,blank=False)
	marks=models.IntegerField(blank=False)
	userid=models.CharField(max_length=120,blank=False)


	def __unicode__(self):
		return self.name

# class Login(models.Model):
# 	fullname = models.CharField(max_length=120,blank=False)
# 	password = models.CharField(max_length=120,blank=False)
