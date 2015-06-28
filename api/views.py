from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import SourcesSerializer,CategoriesSerializer,UserSerializer,UserProfileSerializer, AdvertisingSerializer
from api.models import Categories,Sources,UserProfile,Advertising
from api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.core.mail import send_mass_mail
from django.core.mail import send_mail
import feedparser
import random
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,IsOwner)
	allowed_methods = ('GET',)

class CategoriesViewSet(viewsets.ModelViewSet):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	permission_classes = [IsAuthenticated]
	allowed_methods = ('GET',)
	@detail_route(methods=['post'])
	def addSubscriber(self, request, pk=None):
		category = self.get_object()
		category.subscribers.add(request.user)
		return Response(status=201)
	@detail_route(methods=['post'])
	def removeSubscriber(self, request, pk=None):
		category = self.get_object()
		category.subscribers.remove(request.user)
		return Response(status=201)

class SourcesViewSet(viewsets.ModelViewSet):
	queryset = Sources.objects.all()
	serializer_class = SourcesSerializer
	permission_classes = [IsAuthenticated]
	allowed_methods = ('GET',)

class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = [IsAuthenticated]
	allowed_methods = ('GET','PUT','OPTIONS',)

class CurrentUserView(viewsets.ViewSet):
	#permission_classes = [IsAuthenticated]
	def getProfile(self,request):
		try:
			userProfile = UserProfile.objects.get(user = request.user.id)
		except Exception as e:
			userProfile = UserProfile(request.user.id)
			userProfile.save()
		return Response(UserProfileSerializer(userProfile).data)
	def getCurrent(self,request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)
	def sendMail(self,request):
		# Inicializar variables de correo
		subject = 'Últimas noticias de esta semana'
		message = ''
		messageList = ()

		# Obtener últimas noticias 
		categories = Categories.objects.all()
		for category in categories:
			message = '\n'+category.name+': \n'
			for source in category.sources.all():
				feed_items = feedparser.parse(source.rss_url)
				try:
					for i in range(0,3):
						message +=  feed_items['entries'][i].title + ' - ' + feed_items['entries'][i].link + '\n'
				except Exception as e:
					e
			category.message = message
		# Obtener usuarios suscritos y asignar las categorías correspondientes a su correo
		userProfiles = UserProfile.objects.all()
		for userProfile in userProfiles:
			if userProfile.mailFlag:
				message = ''
				user = User.objects.get(id = userProfile.user.id)
				for category in categories:
					if category.sources:
						message += category.message
				mail = (subject,message,'proyectodsucab@gmail.com',[user.email])
				messageList += mail
		send_mass_mail((messageList,),fail_silently=False)
		return Response(status=201)

class AdvertisingViewSet(viewsets.ModelViewSet):
	queryset = Advertising.objects.all()
	serializer_class = AdvertisingSerializer
	#permission_classes = [IsAuthenticated]
	allowed_methods = ('GET',)
	@list_route(methods=['get'])
	def getAdvertising(self,request,pk=None):
		advertising = Advertising.objects.all()[random.randint(0, Advertising.objects.count() - 1)]
		advertising.views += 1
		advertising.save()
		serializer = AdvertisingSerializer(advertising)
		return Response(serializer.data)
	@detail_route(methods=['get'])
	def clickAdvertising(self,request,pk=None):
		advertising = self.get_object()
		advertising.clicks += 1
		advertising.save()
		return Response(status=201)