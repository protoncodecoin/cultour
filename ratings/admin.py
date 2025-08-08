from django.contrib import admin

from ratings.models import Rating


# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["user", "rating", "content_type", "object_id", "content_object"]
    list_filter = ["object_id"]
    search_fields = ["comment"]
