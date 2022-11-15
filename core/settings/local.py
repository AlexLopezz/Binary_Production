from .base import *
import os
DEBUG = True

ALLOWED_HOSTS = ['localhost','binarysystem.pythonanywhere.com','http://localhost:8080/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')