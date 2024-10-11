from django.shortcuts import redirect


class TokenRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, есть ли токен в сессии
        token = request.session.get('token')

        # Если нет токена и не находимся на странице входа, перенаправляем на страницу входа
        if not token and request.path != '/login/':
            return redirect('/login/')

        return self.get_response(request)
