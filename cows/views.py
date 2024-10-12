import jwt
import datetime
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Cow
from django.contrib import messages


class LoginView(View):
    @staticmethod
    def get(request):
        # Отправляем HTML-форму для логина
        return render(request, 'cows/login.html')

    @staticmethod
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = jwt.encode({
                'username': user.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Время жизни токена 1 час
            }, settings.SECRET_KEY, algorithm='HS256')
            request.session['token'] = token
            return redirect('/')
        # return JsonResponse({'error': 'Invalid credentials'}, status=400)
        messages.error(request, "Неверное имя пользователя или пароль")
        return render(request, 'cows/login.html')


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
