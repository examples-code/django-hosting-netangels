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
        "NAME": str(os.environ["POSTGRES_DB"]),
        "USER": str(os.environ["DBUSER"]),
        "PASSWORD": str(os.environ["DBPASS"]),
        "HOST": str(os.environ.get("DBHOST", "localhost")),
        "PORT": str(os.environ.get("DBPORT", "5432")),
    }
}
