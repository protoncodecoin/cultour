"""
URL configuration for cultour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("restaurants.api.urls", namespace="api")),
    path("api/ratings/", include("ratings.api.urls", namespace="ratings")),
    path("api/hotels/", include("hotels.api.urls", namespace="hotels_api")),
    path("api/payment/", include("payment.api.urls", namespace="payments")),
    path("", include("tours.urls", namespace="tours")),
    path("api/tours/", include("tours.api.urls", namespace="tours_api")),
    path("hotels/", include("hotels.urls", namespace="hotels")),
    path("restaurants/", include("restaurants.urls", namespace="restaurants")),
    path("gallery/", include("gallery.urls", namespace="gallery")),
    path("festivals/", include("festivals.urls", namespace="festivals")),
    path("auth/", include("users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
