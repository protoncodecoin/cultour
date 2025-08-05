# urls.py
from django.urls import path
from .views import HotelReservationAPIView

app_name = "hotels_api"

urlpatterns = [
    path(
        "reservations/",
        HotelReservationAPIView.as_view(),
        name="hotel-reservation",
    ),
]
