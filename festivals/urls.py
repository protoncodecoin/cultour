from django.urls import path

from . import views

app_name = "festivals"

urlpatterns = [
    path("", views.FestivalList.as_view(), name="festivals"),
    path(
        "detail_festival/<int:pk>/",
        views.FestivalDetailView.as_view(),
        name="detail_festival",
    ),
]
