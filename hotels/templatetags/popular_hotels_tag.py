from django import template

from hotels.models import Hotel, HotelRoom

register = template.Library()


@register.inclusion_tag("hotel/fragment/popular_hotels.html")
def show_popular_hotels(count=5):
    hotels = Hotel.objects.all()[:count]
    # rooms = HotelRoom.objects.filter(hotel=hotel_obj)[:count]
    return {"hotels": hotels}
