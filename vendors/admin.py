from django.contrib import admin
from .models import Vendor, Entity

# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name1', 'ent_name', 'state')

admin.site.register(Vendor)
admin.site.register(Entity)
