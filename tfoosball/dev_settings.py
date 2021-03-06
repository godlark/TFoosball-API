from tfoosball.common_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7d!g5l*3nm1=2s@&%11d+jz_$#ii2bugj+9ynhq&cfl0r%pnn)'
DEBUG = True
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# DATABASE
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS
# ------------------------------------------------------------------------------

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:3000',
    '127.0.0.1:3000',
    '127.0.0.1:8000',
)

# LOGGING
# ------------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'matches.log'),
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'tfoosball.matches': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        }
    },
}
