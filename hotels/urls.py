from django.urls import path
from . import views

app_name = "hotels"

urlpatterns = [
    path("", views.HotelListView.as_view(), name="hotels"),
    path("<int:pk>/", views.HotelDetailView.as_view(), name="hotel_detail"),
    path("<int:pk>/rooms/", views.RoomListView.as_view(), name="rooms"),
    path(
        "<int:pk>/rooms/<int:room_pk>/",
        views.RoomDetailView.as_view(),
        name="room_detail",
    ),
]
