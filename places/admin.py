from django.contrib import admin

from places.models import City, State

# Register your models here.


# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ["name", "currency", "createdon", "updatedon"]
#     list_filter = ["name", "createdon", "updatedon"]
#     ordering = ["createdon", "updatedon"]
#     search_fields = ["name"]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "createdon", "updatedon"]
    list_filter = ["name", "createdon", "updatedon"]
    search_fields = ["name"]
    ordering = ["createdon", "updatedon"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "state", "createdon", "updatedon"]
    list_filter = ["name", "state", "createdon", "updatedon"]
