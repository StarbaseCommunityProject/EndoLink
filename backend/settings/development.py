from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9sp3328n!ha1ico2w@p1e7e5h@e7(p&_rk$2v3_4e=n=t0qwqk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['anon'] = '1000/minute'
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['user'] = '1000/minute'
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['register'] = '1000/minute'
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['faction_registration'] = '1000/minute'
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['logout'] = '1000/minute'
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['account_edit'] = '1000/minute'

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(days=100)
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = timedelta(days=100)
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
