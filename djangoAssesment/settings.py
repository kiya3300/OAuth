"""
Django settings for djangoAssesment project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_SECRET = os.getenv('GOOGLE_SECRET')
print(GOOGLE_CLIENT_ID)
print(GOOGLE_SECRET)

FACEBOOK_CLIENT_ID = os.getenv('FACEBOOK_CLIENT_ID')
FACEBOOK_SECRET = os.getenv('FACEBOOK_SECRET')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i5r1cy1-2+v7iob0m9&zrzb!!2#&e^##qryuz19v-o=p#_l!m2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'djangoAssesment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoAssesment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
    'DEFAULT_INFO': 'your_project.urls.swagger_info',  # function returning dict
}

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# SITE_ID = 1

# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_QUERY_EMAIL = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        
        'APP': {
            'client_id': GOOGLE_CLIENT_ID,
            'secret': GOOGLE_SECRET,
            'key': ''
        }
    },

    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'APP': {
            'client_id': FACEBOOK_CLIENT_ID,
            'secret': FACEBOOK_SECRET,
        }
    }

}