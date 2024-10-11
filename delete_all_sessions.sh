if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "The virtual environment is not activated."
    echo "Activating the virtual environment..."
    source .venv/bin/activate
else
    echo "The virtual environment is already activated: $VIRTUAL_ENV"
fi
echo "Deleting all sessions..."
echo "from django.contrib.sessions.models import Session; Session.objects.all().delete()" | python3 manage.py shell
echo "OK."
