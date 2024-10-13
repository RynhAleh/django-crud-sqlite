from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.urls import reverse_lazy
from .models import Cow
from .filters import CowFilter
from django.core.paginator import Paginator
from django.shortcuts import render


def cow_view(request):
    dic = {
        "name": request.GET.get("name", ""),
        "color": request.GET.get("color", ""),
        "breed": request.GET.get("breed", ""),
        "features": request.GET.get("features", ""),
        "srt": request.GET.get("srt", "id"),
        "page": request.GET.get("page", "1"),
        "per": request.GET.get("per", "10"),
    }
    query_list = Cow.objects.order_by(dic["srt"])
    apps_platform_filter = CowFilter(request.GET, queryset=query_list)
    paginator = Paginator(apps_platform_filter.qs, per_page=dic["per"])
    page_obj = paginator.get_page(dic["page"])

    dic.update({
        "page_obj": page_obj,
        "form": apps_platform_filter.form, })

    return render(request, "cows/cow_list.html", dic)


class CowDetail(DetailView):
    model = Cow


class CowCreate(CreateView):
    model = Cow
    fields = ['name', 'color', 'breed', 'features']
    success_url = reverse_lazy('cows:cow_list')


class CowUpdate(UpdateView):
    model = Cow
    fields = ['name', 'color', 'breed', 'features']
    success_url = reverse_lazy('cows:cow_list')


class CowDelete(DeleteView):
    model = Cow
    success_url = reverse_lazy('cows:cow_list')
