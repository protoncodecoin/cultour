from django.shortcuts import render
from django.views.generic import ListView, DetailView

from hotels.models import Hotel


# Create your views here.


class HotelListView(ListView):
    queryset = Hotel.objects.all()
    context_object_name = "hotels"
    paginate_by = 10
    template_name = "hotel/hotels.html"


class HotelDetailView(DetailView):
    """
    Display hotel detail page.
    """

    queryset = Hotel.objects.all()
    context_object_name = "booking"
    template_name = "hotel/hotel_detail.html"
