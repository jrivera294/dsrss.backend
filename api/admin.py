from django.contrib import admin
from api.models import Categories,Sources,Advertising

# Register your models here.

admin.site.register(Sources)
admin.site.register(Categories)
admin.site.register(Advertising)
