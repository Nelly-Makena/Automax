from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'vin')

admin.site.register(Listing, ListingAdmin)
