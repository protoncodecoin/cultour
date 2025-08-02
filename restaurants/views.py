from django.shortcuts import render

from django.views.generic import ListView, DetailView

from restaurants.models import Restaurant


# Create your views here.


class RestaurantListView(ListView):
    queryset = Restaurant.objects.all()
    context_object_name = "restaurants"
    paginate_by = 10
    template_name = "restaurant/restaurant_list.html"


class RestaurantDetailView(DetailView):
    """
    Display restaurant detail page.
    """

    queryset = Restaurant.objects.all()
    context_object_name = "restaurant"
    template_name = "restaurant/restaurant_detail.html"
