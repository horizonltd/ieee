from django.contrib import admin
from . models import Members, TypeOfMembership
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class TypeOfMembershipAdmin(admin.ModelAdmin):
    search_fields = ['__all__']



admin.site.register(Members, MemberAdmin)
admin.site.register(TypeOfMembership, TypeOfMembershipAdmin)