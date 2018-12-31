from django.contrib import admin

from .models import *

# Register your models here.


class VisitorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'access_index')


admin.site.register(VisitorRecord, VisitorRecordAdmin)
