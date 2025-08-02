from django.shortcuts import render

from django.views.generic import ListView, DetailView

from places.models import City, State
from tours.models import TourSite


# Create your views here.
def index(request):
    return render(request, "common/index.html")


def about(request):
    return render(request, "common/about.html")


def contact_us(request):
    return render(request, "common/contact.html")


class TourListView(ListView):
    queryset = TourSite.objects.all()
    context_object_name = "toursites"
    paginate_by = 10
    template_name = "tours/toursites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        return context


class TourDetailView(DetailView):
    """
    Display tour detail page.
    """

    queryset = TourSite.objects.all()
    context_object_name = "toursite"
    template_name = "tours/toursite_detail.html"
