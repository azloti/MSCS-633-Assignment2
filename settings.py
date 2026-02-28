from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "assignment3-dev-key"
DEBUG = True

INSTALLED_APPS = [
    "chatterbot.ext.django_chatterbot",
    "chat",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
