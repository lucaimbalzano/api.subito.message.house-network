#!/bin/bash 
echo "STEP#MIGRATION"
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "STEP#SUSER"
# Run Django management command to create superuser using environment variables
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell

echo "STEP#DEPLOY"
python manage.py runserver 0.0.0.0:8000