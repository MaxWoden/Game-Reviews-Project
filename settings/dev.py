from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# PostgreSQL для разработки
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'game_reviews_db',
        'USER': 'postgres',
        'PASSWORD': 'b89G28Kau',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}