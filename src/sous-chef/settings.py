# -*- coding: utf-8 -*-
"""
Django settings for sous-chef project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '15ine$#^qas4_h2u7yk&lxat*&g*b8+)@wp$2x@vi2#v9)i2#u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This IP may change for different computers and should be the
# request.META.get('REMOTE_ADDR') for your local computer.
# Don't run with this in production and don't
# commit any changes to this INTERNAL_IPS settings.
# WE NEED THIS IN ORDER TO USE 'debug' IN TEMPLATES!!!
INTERNAL_IPS = ['172.19.0.1']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meal',
    'member',
    'order',
    'notification',
    'page',
    'delivery',
    'formtools',
    'django_filters',
    'annoying',
    'leaflet',
    'note',
    'billing',
    'datamigration',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'sous-chef.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/sous-chef/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sous-chef.context_processors.total',
            ],
        },
    },
]

WSGI_APPLICATION = 'sous-chef.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feast',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'db',
        'port': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

LOGIN_URL = reverse_lazy('page:login')
LOGIN_REDIRECT_URL = reverse_lazy('page:home')


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# List of supported languages
LANGUAGES = (
    ('fr', 'Français'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    'meal/locale/',
    'member/locale/',
    'notification/locale/',
    'order/locale/',
    'page/locale/',
    'delivery/locale/',
    'billing/locale',
    'note/locale',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    BASE_DIR + '/sous-chef/static/',
)
STATIC_URL = '/static/'
