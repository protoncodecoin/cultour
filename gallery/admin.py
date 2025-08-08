from django.contrib import admin

from .models import Gallery, Media


# Register your models here.
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["uploaded_on", "caption"]
    list_filter = ["uploaded_on", "caption"]
    search_fields = ["uploaded_on", "caption"]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["created_on"]
