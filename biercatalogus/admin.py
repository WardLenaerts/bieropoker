from django.contrib import admin

from .models import Bier, BierConsumptie, BierFles

admin.site.register(Bier)
admin.site.register(BierConsumptie)
admin.site.register(BierFles)