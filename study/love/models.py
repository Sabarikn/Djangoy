from django.db import models

# Create your models here.
class Tweet(models.Model):
	fullname = models.CharField(max_length=120,blank=False)
