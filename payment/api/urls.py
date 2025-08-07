from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("verify/", views.VerifyPayment.as_view(), name="verify_payment"),
]
