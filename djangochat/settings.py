# Core project configuration: installed apps, database, templates, static, etc.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # project root

SECRET_KEY = 'awy-@gjkx%qk0v4nixzhhk8cl(gnhii)&)-vbbw)r(0a5s&)^y'  # replace in production
DEBUG = True  # development on
ALLOWED_HOSTS = []  # add hosts/IPs in deployment

INSTALLED_APPS = [
    'django.contrib.admin',     # admin site
    'django.contrib.auth',      # auth system
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',                     # your chat app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangochat.urls'  # root URL router

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # project-level templates directory
        'APP_DIRS': True,                  # also load app templates if present
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

WSGI_APPLICATION = 'djangochat.wsgi.application'  # for WSGI servers (gunicorn, etc.)
# If using ASGI/Channels later, ASGI_APPLICATION is in asgi.py.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # simple dev DB
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []  # keep simple for demo

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # silences W042 warnings
