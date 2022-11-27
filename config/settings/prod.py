from .base import *

DEBUG = int(os.environ.get('DEBUG', default=0))

SECRET_KEY = str(os.environ["SECRET_KEY"])

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    default='localhost 127.0.0.1 [::1]'
).split(" ")


INSTALLED_APPS += [

]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": str(os.environ["DBNAME"]),
        "USER": str(os.environ["DBUSER"]),
        "PASSWORD": str(os.environ["DBPASS"]),
        "HOST": str(os.environ.get("DBHOST", "localhost")),
        "PORT": str(os.environ.get("DBPORT", "5432")),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(str(os.environ["WWW_DIR"]), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(str(os.environ["WWW_DIR"]), 'media')
