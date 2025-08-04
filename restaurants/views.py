from django.shortcuts import render

from django.views.generic import ListView, DetailView

from restaurants.models import Restaurant, RestaurantFood, RestaurantTable


# Create your views here.


class RestaurantListView(ListView):
    queryset = Restaurant.objects.all()
    context_object_name = "restaurants"
    paginate_by = 10
    template_name = "restaurant/restaurant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "restaurant"
        return context


class RestaurantDetailView(DetailView):
    """
    Display restaurant detail page.
    """

    # queryset = Restaurant.objects.all()
    model = Restaurant
    context_object_name = "restaurant"
    template_name = "restaurant/restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "restaurant"
        context["foods"] = RestaurantFood.objects.filter(restaurant=self.object)
        context["tables"] = RestaurantTable.objects.filter(restaurant=self.object)
        return context
