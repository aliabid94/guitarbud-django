from django.db import models

# Create your models here.
class Song(models.Model):
	name = models.CharField(max_length=100)
	urlname = models.CharField(max_length=100)
	artist = models.CharField(max_length=100)
	tab = models.CharField(max_length=10000)
	points = models.IntegerField(default=0)
	def __str__(self):
		return self.name
