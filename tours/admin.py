from django.contrib import admin

# Register your models here.
from .models import Tour, TourReservation, TourSite, TourSiteOwner


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["site", "fee", "start_datetime", "end_datetime"]
    list_filter = ["start_datetime", "end_datetime", "fee"]
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


@admin.register(TourReservation)
class TourReservationAdmin(admin.ModelAdmin):
    list_display = ["tourist", "tour", "guests", "is_paid", "created_on"]
    list_filter = ["is_paid", "created_on"]
    search_fields = ["notes"]
