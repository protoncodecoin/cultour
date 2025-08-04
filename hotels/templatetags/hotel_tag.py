from django import template

from hotels.models import Hotel, HotelRoom

register = template.Library()


@register.inclusion_tag("hotel/fragment/related_rooms.html")
def show_hotel_related_rooms(hotel_id, count):
    hotel_obj = Hotel.objects.filter(id=hotel_id).first()
    rooms = HotelRoom.objects.filter(hotel=hotel_obj)[:count]
    return {"hotel_rooms": rooms, "hotel_id": hotel_id}
