from django.contrib import admin

# Register your models here.
from .models import Tour, TourSite, TourSiteOwner


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["site", "city", "fee", "start_datetime", "end_datetime"]
    list_filter = ["start_datetime", "end_datetime", "city", "fee"]
    search_fields = ["notes"]


@admin.register(TourSite)
class TourSiteAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "city",
        "rating",
        "createdon",
        "updatedon",
    ]
    list_filter = ["name", "city", "rating", "createdon", "updatedon"]
    search_fields = ["name", "city"]
