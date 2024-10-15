from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Cow
from .filters import CowFilter
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import CowForm
from django.db.models.deletion import RestrictedError
from cattle_management.settings import ROWS_PER_PAGE


def cow_view(request):
    dic = {
        "name": request.GET.get("name", ""),
        "color": request.GET.get("color", ""),
        "breed": request.GET.get("breed", ""),
        "features": request.GET.get("features", ""),
        "srt": request.GET.get("srt", "id"),
        "page": request.GET.get("page", "1"),
        "per": request.GET.get("per", str(ROWS_PER_PAGE)),
    }
    query_list = Cow.objects.order_by(dic["srt"])
    obj_filter = CowFilter(request.GET, queryset=query_list)
    paginator = Paginator(obj_filter.qs, per_page=dic["per"])
    page_obj = paginator.get_page(dic["page"])

    dic.update({
        "page_obj": page_obj,
        "form": obj_filter.form, })

    return render(request, "cows/cow_list.html", dic)


class CowDetail(DetailView):
    model = Cow
    success_url = reverse_lazy('cows:cow_detail')


def cow_create(request):
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('cows:cow_list'))
            return HttpResponseRedirect(previous_url)
    else:
        form = CowForm()
        return render(request, 'cows/cow_form.html',{'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('cows:cow_list'))})


def cow_update(request, pk):
    obj = get_object_or_404(Cow, pk=pk)

    if request.method == 'POST':
        form = CowForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('cows:cow_list'))
            return HttpResponseRedirect(previous_url)
    else:
        form = CowForm(instance=obj)
        return render(request, 'cows/cow_form.html', {'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('cows:cow_list'))})


def cow_delete(request, pk):
    obj = get_object_or_404(Cow, pk=pk)
    message = {'text': f'Вы действительно хотите удалить КРС (id {obj.pk} - кличка/номер: {obj.name})?'}
    previous_url = ''

    if request.method == 'POST':
        try:
            previous_url = request.POST.get('previous_url', reverse_lazy('cows:cow_list'))
            obj.delete()
            return HttpResponseRedirect(previous_url)
        except RestrictedError:
            message['error'] = "Невозможно удалить КРС, так как на него ссылаются другие записи!"
            return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': previous_url})
    else:
        return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('cows:cow_list'))})
