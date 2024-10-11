#!/bin/bash

# Kill any process related to 'runserver'
kill $(ps aux | grep '[r]unserver' | awk '{print $2}')

# Check if a virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "The virtual environment is not activated."

    # Check if the .venv directory exists
    if [[ ! -d ".venv" ]]; then
        echo "The .venv directory does not exist. Creating a virtual environment..."
        puthon3 -m venv .venv
    else
        echo "The .venv directory already exists."
    fi

    # Activate the virtual environment
    echo "Activating the virtual environment..."
    source .venv/bin/activate
    echo "The virtual environment is now activated."
else
    echo "The virtual environment is already activated: $VIRTUAL_ENV"
fi

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Running migrations..."
puthon3 manage.py makemigrations
puthon3 manage.py migrate

# Start the Django development server
puthon3 manage.py runserver