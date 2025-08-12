from django.contrib import admin

from hotels.models import AvailabilityRequest, Hotel, HotelReservation, HotelRoom


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "name",
        "city",
        "address",
        # "average_rating",
        "createdon",
        "updatedon",
    ]
    list_filter = [
        "city",
        # "ratings",
        "createdon",
        "updatedon",
    ]
    search_fields = ["notes", "address"]
    ordering = ["createdon", "updatedon"]


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ["hotel", "name", "fee", "average_rating", "createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]
    search_fields = ["address", "name", "fee", "notes"]


@admin.register(HotelReservation)
class HotelReservationAdmin(admin.ModelAdmin):
    list_display = [
        "hotel",
        "room",
        "guests",
        "check_in",
        "check_out",
        "status",
        "created_on",
        "updated_on",
    ]
    list_filter = ["check_in", "check_out", "status", "created_on", "updated_on"]
    search_fields = ["special_requests"]


@admin.register(AvailabilityRequest)
class AvailabilityRequestAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "date_from",
        "date_to",
        "guests",
        "children",
        "created_at",
        "hotel",
    ]
    list_filter = ["date_from", "date_to", "created_at"]
