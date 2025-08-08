from typing import Any
from django.shortcuts import render
from django.db.models import Q

from django.views.generic import ListView, DetailView


from festivals.models import Festival
from hotels.models import Hotel
from places.models import State
from restaurants.models import Restaurant
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
        context["tours"] = Tour.objects.filter(site=self.object)
        context["current_page"] = "tour"
        return context


def tour_search(request):
    query = None
    results = []
    result_dict: dict[str, Any | None] = dict()

    # tours
    # restaurants
    # festivals
    # hotels

    if request.method == "GET":
        search = request.GET.get("search")
        state_id = request.GET.get("selected_state")

        # TourSites
        query_rs = TourSite.objects.filter(city__state__id__exact=state_id).filter(
            name__icontains=search
        )
        if len(query_rs) == 0:
            result_dict["toursites"] = None
        else:
            result_dict["toursites"] = query_rs

        # Festivals
        query_rs = Festival.objects.filter(city__state__id__exact=state_id).filter(
            name__icontains=search
        )
        if len(query_rs) == 0:
            result_dict["festivals"] = None
        else:
            result_dict["festivals"] = query_rs

        # Hotels
        query_rs = Hotel.objects.filter(city__state__id__exact=state_id).filter(
            name__icontains=search
        )
        if len(query_rs) == 0:
            result_dict["hotels"] = None
        else:
            result_dict["hotels"] = query_rs

        # Restaurants
        query_rs = Restaurant.objects.filter(city__state__id__exact=state_id).filter(
            name__icontains=search
        )
        if len(query_rs) == 0:
            result_dict["restaurants"] = None
        else:
            result_dict["restaurants"] = query_rs

        # add query to the context for the frontend
        result_dict["query"] = search

    return render(
        request, "common/search_result.html", context={"search_results": result_dict}
    )


# def gallery(request):
#     return render(request, "common/gallery.html")
