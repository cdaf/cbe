"""
Django settings for cbe project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!vv05q%k$8nhc6t&*2u4yxd_wplret8@gajcng%q@x4@fmhvuq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'rest_framework',
    'gm2m',
    'cbe.location',
    'cbe.party',
    'cbe.business_interaction',
    'cbe.customer',
    'cbe.credit',
    'cbe.physical_object',
    'cbe.supplier_partner',
    'cbe.human_resources',
    'cbe.resource',
    'cbe.trouble',
    'cbe.information_technology',
    'cbe.project',
    'cbe.accounts_receivable',
)

#python manage.py makemigrations location party customer credit physical_object supplier_partner human_resources resource trouble information_technology project accounts_receivable

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cbe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cbe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ],
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'cbe.utils.api.BrowsableAPIRendererWithoutForms',
        'cbe.utils.api.PaginatedCSVRenderer',
    ),
}

MQ_FRAMEWORK = {
    'HOST': 'None',
    'USER': 'None',
    'PASSWORD': 'None',
    'EXCHANGE_PREFIX': 'notify.',
    'HTTP_REST_CONTEXT': {
        'SERVER_NAME': '127.0.0.1',
        'SERVER_PORT': 8000,
    }
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    # '--with-coverage',
    # '--cover-package=cbe.location,cbe.party,cbe.business_interaction,cbe.customer,cbe.trouble',
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# LimitDepthMixin serializer setting
DEPTH_MAX = 2

# Try to use a local settings file if available
try:
    from cbe.local_settings import *
except ImportError:
    pass
