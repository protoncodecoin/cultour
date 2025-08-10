import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from storages.backends.s3boto3 import S3Boto3Storage

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Core settings
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "0").lower() in ["true", "t", "1"]
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split()

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    # your apps...
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Serve static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cultour.urls"
WSGI_APPLICATION = "cultour.wsgi.application"

# Database
DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600),
}

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Static Files via Whitenoise ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# --- AWS S3 Credentials (Media) ---
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", None)
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False


# --- Custom S3-backed Media Storage ---
class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False


# --- Modern Storage Configuration ---
STORAGES = {
    "default": {
        "BACKEND": "cultour.settings.PublicMediaStorage",
        "OPTIONS": {
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"

# Other settings like auth validators, REST framework, etc...
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACK_SECRET_KEY")
PAYSTACK_PUBLIC_KEY = os.environ.get("PAYSTACK_PUBLIC_KEY")
