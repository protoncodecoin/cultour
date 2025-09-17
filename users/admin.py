from django.contrib import admin

from users.models import (
    ContactMessage,
    FestivalOwner,
    HotelOwner,
    RestaurantOwner,
    TourSiteOwner,
    Tourist,
)
from django.contrib.auth.models import User


# @admin.register(User)
# class AdminUser(admin.ModelAdmin):
#     list_display = ["first_name", "last_name", "email", "is_active"]


# Register your models here.
@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ["createdon", "updatedon", "user"]
    list_filter = ["createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]


@admin.register(FestivalOwner)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ["user", "createdon", "updatedon"]
    list_filter = ["createdon"]


@admin.register(TourSiteOwner)
class TourSiteOwnerAdmin(admin.ModelAdmin):
    list_display = ["user", "image", "createdon", "updatedon"]
    list_filter = ["user", "createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]


@admin.register(HotelOwner)
class HotelOwner(admin.ModelAdmin):
    list_display = [
        "user",
        "image",
        "createdon",
        "updatedon",
    ]
    list_filter = ["createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]


@admin.register(RestaurantOwner)
class RestaurantOwner(admin.ModelAdmin):
    list_display = ["user", "image", "createdon", "updatedon"]
    list_filter = ["createdon", "updatedon"]
    ordering = ["createdon", "updatedon"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    list_filter = ["email", "created_at"]
