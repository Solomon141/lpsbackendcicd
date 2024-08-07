from pathlib import Path
from django.utils.timezone import timedelta
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+xw=-!2jggcr2%bxctm^e@81c7)!u-7&*-iqssxx5#kv4i!rv0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

X_FRAME_OPTIONS = 'ALLOW-FROM http://localhost:3000'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'djoser',
    'drf_yasg',
    'debug_toolbar',
    'checklist',
    'checklisttype',
    'customer',
    'customercommonfiles',
    'employeedetail',
    'loan',
    'customermarried',
    'spausedetail',
    'customersingle',
    'collateralcar',
    'delegation',
    # 'loanguarantee',
    'loancomment',
    'loanadditionaldocs',
    'carmodel',
    'carcommonfiles',
    'cargaragevalue',
    'carmanufacturer',
    'carmarketvalue',
    'collateralhome',
    'collateralhomefiles',
    'collateralemployee',
    'collateralemployeefiles',
    'collateralstock',
    'collateralstockfiles',
    'hometype',
    # 'homecommonfiles',
    # 'loandelegationperson',
    # 'loandelegationpersonfiles',
    "loantype",
    'loanguaranteeperson',
    'loanguaranteepersonfiles',
    'surety',
    'loanwitness',
    'loancommittee',
    'jobposition',
    'subcity',
    'woreda',
    'holidays',
    'disbursement',
    'withdrawcustomer',
    'withdrawal',
    'withdrawaldetail',
]

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'http://localhost:3001',
#     'http://localhost:85',
#     'exp://192.168.32.66:8081',
# ]

# CORS_ALLOWED_ORIGINS = ['*']

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:8081",
#     "exp://localhost:8081",
#     "http://192.168.0.7:19006",
#     'http://localhost:19006',
#     'exp://192.168.32.66:8081',
# ]

INTERNAL_IPS = [
    '127.0.0.1'
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Custom-Header',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'lps_django_2024.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'lps_django_2024.wsgi.application'

# Database = # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
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

# Internationalization # https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) # https://docs.djangoproject.com/en/5.0/howto/static-files/
# STATIC_URL = 'static/'
# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Default primary key field type # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
