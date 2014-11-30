from django.db import models

class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=50)
	registration_date = models.DateTimeField()
	rating = models.IntegerField(default=0)
	avatar = models.URLField(max_length=200)
	
class Tags(models.Model):
	text = models.CharField(max_length=50)
	
class Question(models.Model):
	header = models.CharField(max_length=200)
	text = models.CharField(max_length=500)
	date = models.DateTimeField()
	tags = models.ManyToManyField(Tags)
	autor = models.ForeignKey(User)
	rating = models.IntegerField(default=0)

class Answer(models.Model):
	text = models.CharField(max_length=500)
	date = models.DateTimeField()
	autor = models.ForeignKey(User)
	tru = models.BooleanField(default=0)
	rating = models.IntegerField(default=0)

# Create your models here.
