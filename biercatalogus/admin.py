from django.contrib import admin

from .models import Bier, BierConsumptie, BierFles

@admin.register(Bier)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'beercolor', 'percentage', 'quantity', 'available']
    list_filter = ['available','beercolor']
    list_editable = ['quantity', 'available']
    save_as = True


admin.site.register(BierConsumptie)
admin.site.register(BierFles)