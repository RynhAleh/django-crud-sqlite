if [[ -z "$VIRTUAL_ENV" ]]; then source .venv/bin/activate; fi
echo "from django.contrib.sessions.models import Session; Session.objects.all().delete()" | python3 manage.py shell