from django.contrib import admin
from . models import  Other
# Register your models here.


class OtherAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Other, OtherAdmin)