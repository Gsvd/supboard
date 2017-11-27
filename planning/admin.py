from django.contrib import admin
from .models import Planning


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    ordering = ['date']

