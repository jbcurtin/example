import os
import typing

from pathlib import Path

from urllib.parse import urlparse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('WWW_SECRET', 'm)v06zp+y-12lk(qgkq!2u$f-sz7tsu$gkknzsqvtn9@6j9%iw')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DEBUG', 'yes').lower() in ['no']:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'webservice.apps.WebserviceConfig',
    'corsheaders',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sustainability_page.urls'

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

WSGI_APPLICATION = 'sustainability_page.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# postgresql://dbuser:dbpassword@sustainability-page-datastore:5432/dbname

PSQL_URL = os.environ.get('PSQL_URL', None)
if PSQL_URL is None:
    raise NotImplementedError('Missing ENVVar PSQL_URL')

url_parts = urlparse(PSQL_URL)
creds, netloc = url_parts.netloc.split('@', 1)
username, password = creds.split(':', 1)
hostname, port = netloc.split(':', 1)
dbname = url_parts.path.strip('/')

# LEGACY_URL = os.environ.get('LEGACY_URL', None)
# if LEGACY_URL is None:
#     raise NotImplementedError('Missing ENVVar LEGACY_URL')

# legacy_url_parts = urlparse(LEGACY_URL)
# legacy_creds, legacy_netloc = legacy_url_parts.netloc.split('@', 1)
# legacy_username, legacy_password = legacy_creds.split(':', 1)
# legacy_hostname, legacy_port = legacy_netloc.split(':', 1)
# legacy_dbname = legacy_url_parts.path.strip('/')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': dbname,
        'USER': username,
        'HOST': hostname,
        'PASSWORD': password,
        'PORT': int(port),
    },
    # 'legacy': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': legacy_dbname,
    #     'USER': legacy_username,
    #     'PASSWORD': legacy_password,
    #     'PORT': int(legacy_port),
    #     'HOST': legacy_hostname,
    # },
    # 'legacy-staging': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'USER': 'root',
    #     'NAME': 'staging',
    #     'PASSWORD': 'password',
    #     'PORT': 3306,
    #     'HOST': '127.0.0.1',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (34.6857, 135.526),
    'DEFAULT_ZOOM': 16,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 20,
    'SCALE': 'both',
    'ATTRIBUTION_PRIFIX': 'tekson', # attribution of your map
    'RESET_VIEW': False,
        'TILES': [('OpenStreetMap', 'http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          'attribution': '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        }),
        ('Drak Map', 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            'attribution': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            'subdomains': 'abcd',
            'maxZoom': 19
        })],
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'webservice.SusPageUser'
ENCODING = 'utf-8'
PWN = typing.TypeVar('PWN')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'webservice': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        }
    },
}

API_BASE = 'http://localhost:8000'
MEDIA_URL = '/assets/'
MEDIA_ROOT = BASE_DIR
# https://github.com/adamchainz/django-cors-headers#cors_allowed_origins
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True
ALLOWED_HOSTS = []
SESSION_COOKIE_AGE = 36000 # 10 hours
# https://docs.djangoproject.com/en/4.1/howto/csrf/#using-csrf-protection-with-ajax
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173']
if DEBUG is False:
    ALLOWED_HOSTS = ['sustainabi.lity.page']
    MEDIA_URL = None
    MEDIA_ROOT = None
