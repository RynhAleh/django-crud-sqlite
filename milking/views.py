from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Milking
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import MilkingForm
from django.db.models.deletion import RestrictedError
from cattle_management.settings import ROWS_PER_PAGE


def milking_view(request):
    dic = {
        "datetime": request.GET.get("datetime", ""),
        "staff_id": request.GET.get("staff_id", ""),
        "milk_amount_total": request.GET.get("milk_amount_total", ""),
        "cows_milked": request.GET.get("cows_milked", ""),
        "srt": request.GET.get("srt", "id"),
        "page": request.GET.get("page", "1"),
        "per": request.GET.get("per", str(ROWS_PER_PAGE)),
    }
    query_list = Milking.objects.order_by(dic["srt"])
    paginator = Paginator(query_list, per_page=dic["per"])
    page_obj = paginator.get_page(dic["page"])

    dic.update({
        "page_obj": page_obj,
    })

    return render(request, "milking/milking_list.html", dic)


class MilkingDetail(DetailView):
    model = Milking
    success_url = reverse_lazy('milking:milking_detail')


def milking_create(request):
    if request.method == 'POST':
        form = MilkingForm(request.POST)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('milking:milking_list'))
            return HttpResponseRedirect(previous_url)
        else:
            return render(request, 'milking/milking_form.html', {'form': form,'previous_url': request.POST.get('previous_url', reverse_lazy('milking:milking_list'))})
    else:
        form = MilkingForm()
        return render(request, 'milking/milking_form.html',{'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('milking:milking_list'))})


def milking_update(request, pk):
    obj = get_object_or_404(Milking, pk=pk)

    if request.method == 'POST':
        form = MilkingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('milking:milking_list'))
            return HttpResponseRedirect(previous_url)
        else:
            return render(request, 'milking/milking_form.html', {'form': form,'previous_url': request.POST.get('previous_url', reverse_lazy('milking:milking_list'))})
    else:
        form = MilkingForm(instance=obj)
        return render(request, 'milking/milking_form.html', {'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('milking:milking_list'))})


def milking_delete(request, pk):
    obj = get_object_or_404(Milking, pk=pk)
    message = {'text': f'Вы действительно хотите запись (id {obj.pk} - Дата/время: {obj.datetime})?'}
    previous_url = ''
    if request.method == 'POST':
        try:
            previous_url = request.POST.get('previous_url', reverse_lazy('milking:milking_list'))
            obj.delete()
            return HttpResponseRedirect(previous_url)
        except RestrictedError:
            message['error'] = "Невозможно удалить запись дойки, так как на нее ссылаются другие записи!"
            return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': previous_url})
    else:
        return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('milking:milking_list'))})
