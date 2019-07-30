from django.contrib import admin
from . models import AGM
# Register your models here.


class AGMAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(AGM, AGMAdmin)
