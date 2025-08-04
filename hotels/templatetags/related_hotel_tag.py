from django import template

from hotels.models import Hotel, HotelRoom

register = template.Library()


@register.inclusion_tag("hotel/fragment/related_hotels.html")
def show_related_hotels(hotel_id, count=2):
    hotel_query = Hotel.objects.all().exclude(pk=hotel_id)[:count]
    return {"related_hotels": hotel_query}
