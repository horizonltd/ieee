from django.contrib import admin
from . models import  Gallery
# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Gallery, GalleryAdmin)