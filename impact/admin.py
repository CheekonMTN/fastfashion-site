from django.contrib import admin
from .models import HeadlineStat

@admin.register(HeadlineStat)
class HeadlineStatAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "unit", "source")
