from rebecca.settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'rebecca_live',
        'USER': 'rebecca_live',
        'PASSWORD': 'rebecca_live',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '%s/../rebecca-media-live/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'rebecca_live',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../rebecca-media-live/uploads/' % BUILDOUT_PATH

COMPRESS_ENABLED = True
