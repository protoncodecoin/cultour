from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("activation/<uidb64>/<token>/", views.activate, name="activate"),
]
