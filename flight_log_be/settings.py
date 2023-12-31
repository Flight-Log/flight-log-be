"""
Django settings for flight_log_be project.

Generated by "django-admin startproject" using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-kqc0_9jf46slrvrr16kn+g(yiyj7idjk@*fa+*a=r6%6t5du1y"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# define heroku environment
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ


# Application definition

INSTALLED_APPS = [
    "rest_framework",
    # "rest_framework_json_api",
    "flight_log_be",
    "psycopg2",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Restrict CORS access for all domains pre-deployment
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
  'http://localhost:19006',
  'http://localhost:19000',
  'https://flight-log-ui-hjawad22-flightlog.vercel.app',
  'https://flight-log-six.vercel.app'
]

ROOT_URLCONF = "flight_log_be.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "flight_log_be.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "FlightLog",
        "USER": "flightlog",
        "PASSWORD": "flightlog",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "FlightLog",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
elif IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # REST Framework Settings for REST Framework JSON API
# REST_FRAMEWORK = {
#     "PAGE_SIZE": 10,
#     "EXCEPTION_HANDLER": "rest_framework_json_api.exceptions.exception_handler",
#     "DEFAULT_PAGINATION_CLASS": "rest_framework_json_api.pagination.JsonApiPageNumberPagination",
#     "DEFAULT_PARSER_CLASSES": (
#         "rest_framework_json_api.parsers.JSONParser",
#         "rest_framework.parsers.FormParser",
#         "rest_framework.parsers.MultiPartParser",
#     ),
#     "DEFAULT_RENDERER_CLASSES": (
#         "rest_framework_json_api.renderers.JSONRenderer",
#         # If you're performance testing, you will want to use the browseable API
#         # without forms, as the forms can generate their own queries.
#         # If performance testing, enable:
#         # "example.utils.BrowsableAPIRendererWithoutForms",
#         # Otherwise, to play around with the browseable API, enable:
#         "rest_framework_json_api.renderers.BrowsableAPIRenderer",
#     ),
#     "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",
#     "DEFAULT_SCHEMA_CLASS": "rest_framework_json_api.schemas.openapi.AutoSchema",
#     # Comment this section out or add additional configuration
#     # "DEFAULT_FILTER_BACKENDS": (
#     #     "rest_framework_json_api.filters.QueryParameterValidationFilter",
#     #     "rest_framework_json_api.filters.OrderingFilter",
#     #     "rest_framework_json_api.django_filters.DjangoFilterBackend",
#     #     "rest_framework.filters.SearchFilter",
#     # ),
#     "SEARCH_PARAM": "filter[search]",
#     "TEST_REQUEST_RENDERER_CLASSES": (
#         "rest_framework_json_api.renderers.JSONRenderer",
#     ),
#     "TEST_REQUEST_DEFAULT_FORMAT": "vnd.api+json",
# }
