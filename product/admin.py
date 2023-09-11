from django.contrib import admin
from . models import products,offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','description','discount')

# Register your models here.

admin.site.register(products,ProductAdmin)
admin.site.register(offer,OfferAdmin)