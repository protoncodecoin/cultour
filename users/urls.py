from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    # path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<int:pk>/", views.DashBoardView.as_view(), name="dashboard"),
    path("activation/<uidb64>/<token>/", views.activate, name="activate"),
    path("contact-us/", views.contact_us, name="contact"),
    path("check-availability", views.check_availability, name="check_availability"),
    path("policies/", views.policies, name="policies"),
]
