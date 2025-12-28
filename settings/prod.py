from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# PostgreSQL для продакшена (можно использовать DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Настройки для статических файлов в продакшене
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'