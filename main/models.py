from django.db import models

# Create your models here.

class Claim(models.Model):
	topic = models.CharField(max_length=256)
	text = models.TextField()
	cabinet = models.IntegerField()
	status = models.IntegerField()
	user = models.CharField(max_length=124)
	firstname = models.CharField(max_length=124)
	lastname = models.CharField(max_length=124)
	assigned = models.CharField(max_length=124)
	assigned_firstname = models.CharField(max_length=124)
	assigned_lastname = models.CharField(max_length=124)