from django.db import models
from datetime import datetime

# Create your models here.
class Angkringan(models.Model):
	name = models.CharField(max_length=255)	# Name of the angkringan

class Message(models.Model):
	text = models.CharField(max_length=255)	# Text which is sent by the user
	date = models.DateTimeField(default=datetime.now, blank=True) # Date the text was sent
	user = models.CharField(max_length=255)	# User's name
	angkringan = models.CharField(max_length=255) # FOREIGN KEY (`name`) REFERENCES `Angkringan` (`name`)