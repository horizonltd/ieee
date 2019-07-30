from django.contrib import admin
from . models import  Downloads
# Register your models here.


class DownloadsAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Downloads, DownloadsAdmin)