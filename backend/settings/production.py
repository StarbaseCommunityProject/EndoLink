from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

ALLOWED_HOSTS.append("www.endo.link")
