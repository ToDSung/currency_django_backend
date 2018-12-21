from django.contrib import admin
from .models import JPY, CNY, USD, EUR, GBP, AUD, SGD
# Register your models here.

@admin.register(JPY)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JPY._meta.fields]

@admin.register(CNY)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CNY._meta.fields]

@admin.register(USD)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in USD._meta.fields]

@admin.register(EUR)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EUR._meta.fields]

@admin.register(GBP)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GBP._meta.fields]

@admin.register(AUD)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AUD._meta.fields]

@admin.register(SGD)
class JPYAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SGD._meta.fields]    

# admin.site.register(JPY)
# admin.site.register(CNY)
# admin.site.register(USD)
# admin.site.register(EUR)
# admin.site.register(GBP)
# admin.site.register(AUD)
# admin.site.register(SGD)
