from django.urls import path

from . import views

app_name = "tours_api"

urlpatterns = [
    path(
        "reservations/",
        views.TourReservationView.as_view(),
        name="tour_reservation_create",
    )
]
