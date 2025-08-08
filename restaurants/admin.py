from django.contrib import admin

from restaurants.models import (
    Restaurant,
    RestaurantFood,
    RestaurantTable,
    TableReservation,
)


# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "name",
        "city",
        "average_rating",
        "createdon",
        "updatedon",
    ]
    list_filter = [
        "owner",
        "createdon",
        "updatedon",
    ]
    search_fields = ["notes", "city", "address"]


@admin.register(RestaurantFood)
class RestaurantFoodAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "name", "price", "rating", "createdon", "updatedon"]
    list_filter = [
        "rating",
        "createdon",
        "updatedon",
    ]

    search_fields = ["price", "notes"]


@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "table_number", "seats", "fee", "is_available"]
    list_filter = ["table_number", "seats", "is_available"]
    search_fields = ["table_number", "seats"]


@admin.register(TableReservation)
class TableReservationAdmin(admin.ModelAdmin):
    list_display = ["table", "reservation_date", "reservation_time", "guests"]
    list_filter = ["reservation_time", "guests", "reservation_date"]

    search_fields = ["guests"]
