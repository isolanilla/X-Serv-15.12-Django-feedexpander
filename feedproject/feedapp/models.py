from django.db import models

# Create your models here.

class Users (models.Model):
    persona = models.CharField(max_length=30)
    

class Mo_Tweets (models.Model):
	name = tweets = models.ForeignKey(Users)
	content = models.CharField(max_length = 150)
	date = models.DateField()
	url = models.CharField(max_length = 64)