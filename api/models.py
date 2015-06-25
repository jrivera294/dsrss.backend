from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=50)
	subscribers = models.ManyToManyField(User,blank=True,related_name='categories')
	def __str__(self):
		return self.name

class Sources(models.Model):
	name = models.CharField(max_length=50,default='')
	rss_url = models.CharField(max_length=255)
	category = models.ForeignKey(Categories,related_name='sources')
	full_content = models.BooleanField(default=False)
	rss_format = models.CharField(max_length=50,default='xml')
	def __str__(self):
		return self.name

class Advertising(models.Model):
	name = models.CharField(max_length=50,default='')
	url = models.CharField(max_length=255)
	img_url = models.CharField(max_length=255)
	clicks = models.BigIntegerField()
	user_clicks = models.ManyToManyField(User,blank=True,related_name='user_clicks')
	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	mailFlag = models.BooleanField(default=False)
	def __str__(self):
		return self.user.username