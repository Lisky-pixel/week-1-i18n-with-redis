from django.contrib import admin
from .models import Produce


@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin_village')
