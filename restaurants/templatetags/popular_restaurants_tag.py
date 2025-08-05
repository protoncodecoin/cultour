import random
from django import template

from restaurants.models import Restaurant

register = template.Library()


@register.inclusion_tag("restaurant/fragment/popular_restaurants.html")
def show_hotel_related_rooms(restaurant_id, count=4):
    # Get all IDs
    ids = list(Restaurant.objects.values_list("id", flat=True))

    # Choose random IDs
    random_ids = random.sample(ids, 2)

    # Get objects with those IDs
    random_objects = Restaurant.objects.filter(id__in=random_ids)
    return {"resturants": random_objects, "restaurant_id": restaurant_id}
