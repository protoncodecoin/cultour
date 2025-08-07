import random
from django import template

from restaurants.models import Restaurant

register = template.Library()


@register.inclusion_tag("restaurant/fragment/popular_restaurants.html")
def show_popular_restaurants():
    # Get all IDs
    # random_objects = Restaurant.objects.filter(id__in=random_ids)
    random_objects = Restaurant.objects.all()[:5]
    print(random_objects)
    return {"restaurants": random_objects}
