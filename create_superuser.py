# app/create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="ititor1210").exists():
    User.objects.create_superuser(
        username="ititor1210",
        email="ititor1210@gmail.com",
        password="shekaru1210"
    )
    print("✅ Superuser created.")
else:
    print("ℹ️ Superuser already exists.")
