import jwt
import datetime
from django.conf import settings
from django.contrib.auth import authenticate
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages


class LoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'cattle_management/login.html')

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
        messages.error(request, "Неверное имя пользователя или пароль")
        return render(request, 'cattle_management/login.html')


def debug_status(request):
    from django.http import JsonResponse
    return JsonResponse({'DEBUG': settings.DEBUG})