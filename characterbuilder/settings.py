"""
Django settings for characterbuilder project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import socket
import psycopg2
import dj_database_url
# from dotenv import load_dotenv
# load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# If the host name starts with 'live', DJANGO_HOST = "production"
if socket.gethostname().startswith('live'):
    DJANGO_HOST = "production"
# Else if host name starts with 'test', set DJANGO_HOST = "test"
elif socket.gethostname().startswith('test'): 
    DJANGO_HOST = "testing"
else:
# If host doesn't match, assume it's a development server, set DJANGO_HOST = "development"
    DJANGO_HOST = "development"
# Define general behavior variables for DJANGO_HOST and all others
if DJANGO_HOST == "production":
    DEBUG = False
    STATIC_URL = 'https://homebrew-character-builder.herokuapp.com/'
else:
    DEBUG = True
    STATIC_URL = '/static/'

# For SASS Compression and Deployment
COMPRESS_OFFLINE = True
LIBSASS_OUTPUT_STYLE = 'compressed'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    'homebrew-character-builder.herokuapp.com',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
    'sass_processor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'characterbuilder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/www/STORE/main_app/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'characterbuilder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'characterbuilder',
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Use Custom User Model
AUTH_USER_MODEL = 'main_app.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

STATIC_ROOT = BASE_DIR / 'static'

SASS_PROCESSOR_ROOT = STATIC_ROOT

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'