from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = 'MAS Database Manager'
admin.site.index_title = 'Administration'

@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit']

@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.MaterialLineItem)
class MaterialLineItemAdmin(admin.ModelAdmin):
    list_display = ['date', 'material_name', 'unit',
        'quantity', 'location', 'remarks']
    
