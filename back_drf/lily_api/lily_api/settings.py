import os
from datetime import timedelta
from pathlib import Path
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')


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
    'rest_framework_simplejwt',

    'orders.apps.OrdersConfig',
    'products.apps.ProductsConfig',
    'users.apps.UsersConfig',
    'clean_db'
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

ROOT_URLCONF = 'lily_api.urls'

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

WSGI_APPLICATION = 'lily_api.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB_LILY'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db_postgres_lily',
        'PORT': '5432',
    },
    'lily': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB_LILY'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db_postgres_lily',
        'PORT': '5432',
    },
    'da': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB_DA'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db_postgres_da',
        'PORT': '5432',
    },
    'bastina': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB_BASTINA'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db_postgres_bastina',
        'PORT': '5432',
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':
        [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ],

    'DEFAULT_AUTHENTICATION_CLASSES':
        [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],

    'DEFAULT_PERMISSION_CLASSES':
        [
            'rest_framework.permissions.IsAuthenticated',
        ],
    'DEFAULT_THROTTLE_CLASSES':
        [
            'rest_framework.throttling.ScopedRateThrottle',
        ],
    'DEFAULT_THROTTLE_RATES': {
            'user_login': '6/minute',
            'user_sign_up': '3/day'
        },
    'DATETIME_FORMAT': "%Y-%m-%d Time %H:%M",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 2,
    # 'DEFAULT_PAGINATION_CLASS': 'products.pagination.ReviewsPagination',
    # 'PAGE_SIZE': 4,
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8081",
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_ALLOWED_ORIGINS = ["http://localhost:8081"]
CORS_ORIGINS_WHITELIST = ["http://localhost:8081"]

CORS_ALLOW_ALL_ORIGINS = False


MEDIA_URL = '/img/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'img')

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'users.backend.CustomAuthBackend'
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup_db'}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=15),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


BASE_URL = os.getenv('BASE_URL')

# Celery settings
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BACKEND = 'redis://redis:6379/0'
CELERY_BROKER = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": 'redis://redis:6379/0',
        "OPTIONS": {
            'db': '1'
        }
    }
}

# HTTPS setup
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
