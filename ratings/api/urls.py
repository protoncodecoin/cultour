# ratings/api/urls.py
from django.urls import path
from .views import SubmitRatingView

app_name = "ratings"

urlpatterns = [
    path("submit-rating/", SubmitRatingView.as_view(), name="submit-rating"),
]
