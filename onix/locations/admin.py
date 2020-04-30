from django.contrib import admin
from .models import City, Country, Symbol


# Register your models here.

@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_filter = ['country']


@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Symbol)
