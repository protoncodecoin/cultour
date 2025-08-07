from django.urls import path

from . import views

app_name = "tours"

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact_us, name="contact"),
    path("tours/", views.TourListView.as_view(), name="tours"),
    path("search/", views.tour_search, name="search"),
    path("tours/<int:pk>/", views.TourDetailView.as_view(), name="tour_detail"),
]
