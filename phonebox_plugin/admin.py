from django.contrib import admin
from .models import Number


@admin.register(Number)
class NumPlanAdmin(admin.ModelAdmin):
    list_display = ("number", "tenant", "description", "ported_out", "ported_out_date", "ported_out_to", "is_owner", "provider", "forward_to")
