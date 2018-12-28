from django.contrib import admin

from .models import *


# Register your models here.


class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name')


admin.site.register(ResourceCategory, ResourceCategoryAdmin)


class NetResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'resource_category', 'display_name')


admin.site.register(NetResource, NetResourceAdmin)
