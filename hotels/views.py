from django.shortcuts import render
from django.views.generic import ListView, DetailView

from hotels.models import Hotel, HotelRoom
from places.models import State


# Create your views here.


class HotelListView(ListView):
    queryset = Hotel.objects.all()
    context_object_name = "hotels"
    paginate_by = 10
    template_name = "hotel/hotels.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "hotel"
        context["states"] = State.objects.all()
        return context


class HotelDetailView(DetailView):
    """
    Display hotel detail page.
    """

    # queryset = Hotel.objects.all()
    model = Hotel
    context_object_name = "hotel"
    template_name = "hotel/hotel_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "hotel"
        context["hotel_pk"] = self.object.pk
        context["rooms"] = HotelRoom.objects.select_related("hotel").filter(
            hotel=self.object
        )

        return context


class RoomListView(ListView):
    queryset = HotelRoom.objects.all()
    context_object_name = "rooms"
    paginate_by = 10
    template_name = "hotel/room_list.html"


class RoomDetailView(DetailView):
    model = HotelRoom
    context_object_name = "room"
    template_name = "hotel/room_detail.html"

    def get_object(self, queryset=None):
        room_pk = self.kwargs["room_pk"]
        return HotelRoom.objects.get(pk=room_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_id"] = self.object.pk
        context["hotel_id"] = self.kwargs["pk"]

        return context
