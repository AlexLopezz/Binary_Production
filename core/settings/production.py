from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'binarysystem$dbSentidos',
        'USER': 'binarysystem',
        'PASSWORD': 'binary2022',
        'HOST': 'binarysystem.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')