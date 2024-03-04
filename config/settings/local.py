from .base import *
import os

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

print("AMBIENTE: LOCAL")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT2 = os.path.join(BASE_DIR, 'media', 'local')
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'statics'))]
