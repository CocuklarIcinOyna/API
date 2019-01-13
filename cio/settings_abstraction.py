#This file provide an abstraction for production and development servers.

ABST_DB = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
}

ABST_SECRET_KEY = ''

ABST_DEBUG = True

ABST_ALLOWED_HOSTS = ['127.0.0.1']
