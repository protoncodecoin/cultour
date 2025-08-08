# ratings/api/urls.py
from django.urls import path
from .views import RatingCreateAPIView

app_name = "ratings"

urlpatterns = [
    path("create-rating/", RatingCreateAPIView.as_view(), name="create-rating"),
]
