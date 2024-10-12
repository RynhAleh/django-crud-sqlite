from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cow


class CowList(ListView):
    model = Cow


class CowDetail(DetailView):
    model = Cow


class CowCreate(CreateView):
    model = Cow
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('cows:cow_list')


class CowUpdate(UpdateView):
    model = Cow
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('cows:cow_list')


class CowDelete(DeleteView):
    model = Cow
    success_url = reverse_lazy('cows:cow_list')
