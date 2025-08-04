from django import template

from festivals.models import Festival

register = template.Library()


@register.inclusion_tag("festivals/fragment/featured_festivals.html")
def show_featured_festivals(count=5):
    featured_festivals = Festival.objects.filter(is_featured=True)[:count]
    return {"featured_festivals": featured_festivals}
