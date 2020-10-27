from .settings import *

print('production server')

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ritma',
        'USER': 'root',
        'HOST': 'localhost',
        'PASSWORD': 'Zomper',
        'PORT': '3306',
    }
}