from django.contrib import admin
from api.models import Categories,Sources,Advertising,UserProfile

# Register your models here.

admin.site.register(Sources)
admin.site.register(Categories)
admin.site.register(Advertising)
admin.site.register(UserProfile)
