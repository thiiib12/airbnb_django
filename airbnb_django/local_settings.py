from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'airbnb_copy',
        'USER': 'thibalex',
        'PASSWORD': 'thibault12',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}