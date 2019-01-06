from django.contrib import admin

from .models import *


# Register your models here.


class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name')


admin.site.register(ResourceCategory, ResourceCategoryAdmin)


class NetResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'resource_category', 'display_name')


admin.site.register(NetResource, NetResourceAdmin)


class OriginalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name')


admin.site.register(OriginalCategory, OriginalCategoryAdmin)


class OriginalResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_category', 'title')


admin.site.register(OriginalResource, OriginalResourceAdmin)
