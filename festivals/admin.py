from django.contrib import admin

from .models import Festival

# Register your models here.


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "name",
        "city",
        "month_of_celebration",
        "category",
        "start_date",
        "end_date",
        "is_approved",
        "is_featured",
    ]
    list_filter = [
        "month_of_celebration",
        "category",
        "start_date",
        "end_date",
        "is_approved",
        "is_featured",
    ]
    search_fields = ["name", "city", "history", "category"]
