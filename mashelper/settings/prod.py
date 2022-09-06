import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
  'default': dj_database_url.config()
}

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


CORS_ALLOWED_ORIGINS = [
  'http://localhost:3000',
  'http://127.0.0.1:3000',
]

RENDER_EXTERNAL_CORS_ORIGINS = os.environ.get('RENDER_EXTERNAL_CORS_ORIGINS')
if RENDER_EXTERNAL_CORS_ORIGINS:
    CORS_ALLOWED_ORIGINS.append(RENDER_EXTERNAL_CORS_ORIGINS)
