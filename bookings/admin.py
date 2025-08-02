from django.contrib import admin

from bookings.models import (
    RestaurantOrder,
    RestaurantOrderFood,
    RoomBooking,
    TourBooking,
)
from restaurants.models import Restaurant


# Register your models here.
@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ["tour", "createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]
    search_fields = ["notes"]
    ordering = ["createdon", "updatedon"]


@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ["room", "createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]


@admin.register(RestaurantOrder)
class RestaurantOrderAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "tourist", "total", "createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]
    search_fields = ["notes"]


@admin.register(RestaurantOrderFood)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["order", "food", "quantity", "total", "createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]
