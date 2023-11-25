# myapp/admin.py

from django.contrib import admin
from .models import State, LGA, Ward, PollingUnit, AnnouncedPuResult, AnnouncedLgaResult

# Register your models with the admin site


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['name', 'lga']


@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'ward']


@admin.register(AnnouncedPuResult)
class AnnouncedPuResultAdmin(admin.ModelAdmin):
    list_display = ['polling_unit', 'party', 'party_score']


@admin.register(AnnouncedLgaResult)
class AnnouncedLgaResultAdmin(admin.ModelAdmin):
    list_display = ['lga', 'party', 'party_score']
