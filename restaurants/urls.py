from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("", views.RestaurantListView.as_view(), name="list_restaurant"),
    path("<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant_detail"),
]
