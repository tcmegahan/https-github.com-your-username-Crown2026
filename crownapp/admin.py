from django.contrib import admin
from .models import School, Family

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'city', 'state', 'created']
    search_fields = ['name', 'code', 'city']
    list_filter = ['state', 'created']

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'email', 'phone', 'school', 'created']
    search_fields = ['last_name', 'email']
    list_filter = ['school', 'created']
    autocomplete_fields = ['school']
