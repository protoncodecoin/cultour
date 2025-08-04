from django import template

from tours.models import TourSite

register = template.Library()


@register.inclusion_tag("tours/fragment/top_tours.html")
def show_top_tours(count=5):
    top_tours_featured = TourSite.objects.filter(is_top_tour=True)[:count]
    return {"top_tours": top_tours_featured}
