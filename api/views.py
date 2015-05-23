from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import SourcesSerializer,CategoriesSerializer,UserSerializer
from api.models import Categories,Sources
from api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
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

class SourcesViewSet(viewsets.ModelViewSet):
	queryset = Sources.objects.all()
	serializer_class = SourcesSerializer
	permission_classes = [IsAuthenticated]
	allowed_methods = ('GET',)