from rebecca.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'rebecca_qa',
        'USER': 'rebecca_qa',
        'PASSWORD': 'rebecca_qa',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '%s/../rebecca-media-qa/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'rebecca_qa',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../rebecca-media-qa/uploads/' % BUILDOUT_PATH
