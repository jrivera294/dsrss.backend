from rest_framework import serializers
from api.models import Categories,Sources,Advertising,UserProfile
from django.contrib.auth.models import User

class SourcesSerializer(serializers.ModelSerializer):
	#category = CategoriesSerializer()
	class Meta:
		model = Sources
		fields = ('id','name','rss_url','full_content','rss_format')

class CategoriesSerializer(serializers.ModelSerializer):
	sources = SourcesSerializer(many=True)
	class Meta:
		model = Categories
		fields = ('id','name','sources')

class UserSerializer(serializers.ModelSerializer):
	categories = CategoriesSerializer(many=True)
	class Meta:
		model = User
		fields = ('id','username','email','categories')

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('user','mailFlag')

class AdvertisingSerializer(serializers.ModelSerializer):
	#category = CategoriesSerializer()
	class Meta:
		model = Advertising
		fields = ('id','name','url','img_url','clicks','views')