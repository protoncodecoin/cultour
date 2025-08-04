from django.shortcuts import render

from django.views.generic import ListView, DetailView


from places.models import State
from tours.models import Tour, TourSite


# Create your views here.
def index(request):
    states = State.objects.all()
    context = {"states": states, "current_page": "home"}
    return render(request, "common/index.html", context=context)


def about(request):
    return render(request, "common/about.html", context={"current_page": "about"})


def contact_us(request):
    return render(request, "common/contact.html", context={"current_page": "contact"})


class TourListView(ListView):
    queryset = TourSite.objects.all()
    context_object_name = "toursites"
    paginate_by = 10
    template_name = "tours/toursites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "tour"
        context["states"] = State.objects.all()
        return context


class TourDetailView(DetailView):
    """
    Display tour detail page.
    """

    queryset = TourSite.objects.all()
    context_object_name = "toursite"
    template_name = "tours/toursite_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "tour"
        return context
