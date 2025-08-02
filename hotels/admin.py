from django.contrib import admin

from hotels.models import Hotel, HotelRoom


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "name",
        "city",
        "address",
        "rating",
        "createdon",
        "updatedon",
    ]
    list_filter = ["city", "rating", "createdon", "updatedon"]
    search_fields = ["notes", "address"]
    ordering = ["createdon", "updatedon"]


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ["hotel", "name", "fee", "rating", "createdon", "updatedon"]
    list_filter = ["rating", "createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]
    search_fields = ["address", "name", "fee", "notes"]
