from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}