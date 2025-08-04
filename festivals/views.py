from django.shortcuts import render

from django.views.generic import ListView, DetailView

from festivals.models import Festival
from places.models import State


# Create your views here.
class FestivalList(ListView):
    queryset = Festival.objects.all()
    context_object_name = "festivals"
    paginate_by = 10
    template_name = "festivals/festival_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        context["current_page"] = "festival"
        return context


class FestivalDetailView(DetailView):
    queryset = Festival.objects.all()
    context_object_name = "festival"
    template_name = "festivals/festival_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "festival"
        return context
