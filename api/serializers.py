from rest_framework import serializers
from api.models import Categories,Sources,Advertising
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

