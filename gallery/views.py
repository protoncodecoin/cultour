from typing import Any
from django.shortcuts import render

from django.views.generic import ListView

from gallery.models import Gallery

# Create your views here.


class GalleryListView(ListView):
    queryset = Gallery.objects.all()
    context_object_name = "gallery_images"
    paginate_by = 10
    template_name = "common/gallery.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "gallery"
        return context
