from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))
DEBUG = True


#STATIC
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

#MEDIA
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

#WSGI
WSGI_APPLICATION = 'config.wsgi.dev.application'


# DB
DATABASES = secrets['DATABASES']
print(DATABASES)