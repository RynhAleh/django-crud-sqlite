from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Staff
from .filters import StaffFilter
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StaffForm
from django.db.models.deletion import RestrictedError


def staff_view(request):
    dic = {
        "lastname": request.GET.get("name", ""),
        "srt": request.GET.get("srt", "id"),
        "page": request.GET.get("page", "1"),
        "per": request.GET.get("per", "10"),
    }
    query_list = Staff.objects.order_by(dic["srt"])
    obj_filter = StaffFilter(request.GET, queryset=query_list)
    paginator = Paginator(obj_filter.qs, per_page=dic["per"])
    page_obj = paginator.get_page(dic["page"])

    dic.update({
        "page_obj": page_obj,
        "form": obj_filter.form, })

    return render(request, "lists/staff_list.html", dic)


class StaffDetail(DetailView):
    model = Staff
    success_url = reverse_lazy('lists:staff_list')


def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('lists:staff_list'))
            return HttpResponseRedirect(previous_url)
    else:
        form = StaffForm()
        return render(request, 'lists/staff_form.html',{'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('lists:staff_list'))})


def staff_update(request, pk):
    obj = get_object_or_404(Staff, pk=pk)

    if request.method == 'POST':
        form = StaffForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            previous_url = request.POST.get('previous_url', reverse_lazy('lists:staff_list'))
            return HttpResponseRedirect(previous_url)
    else:
        form = StaffForm(instance=obj)
        return render(request, 'lists/staff_form.html', {'form': form, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('lists:staff_list'))})


def staff_delete(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    message = {'text': f'Вы действительно хотите удалить сотрудника (id {obj.pk} - {obj.lastname} {obj.firstname} {obj.patronymic})?'}
    previous_url = ''

    if request.method == 'POST':
        try:
            previous_url = request.POST.get('previous_url', reverse_lazy('lists:staff_list'))
            obj.delete()
            return HttpResponseRedirect(previous_url)
        except RestrictedError:
            message['error'] = f"Невозможно удалить сотрудника, так как на него ссылаются другие записи!"
            return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': previous_url})
    else:
        return render(request, 'cattle_management/confirm_delete.html', {'message': message, 'previous_url': request.META.get('HTTP_REFERER', reverse_lazy('cows:cow_list'))})
