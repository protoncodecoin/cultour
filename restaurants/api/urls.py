from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "api"

urlpatterns = [
    path(
        "create-reservation/",
        views.CreateTableReservation.as_view(),
        name="create_reservation",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
