from django.contrib import admin
from . models import Conference, Agenda, Icon
# Register your models here.


class ConferenceAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class AgendaAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class IconAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Icon, IconAdmin)