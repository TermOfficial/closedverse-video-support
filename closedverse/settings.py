"""
Local settings for Closedverse.

Everything set here overrides the values set in settings_default.py.

View that file for information on what these keys are for.
"""

# This line imports default settings and is required.
from .settings_default import *

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The secret key is set by a "SECRET_KEY" environment variable
# example: ... SECRET_KEY=my-secret ./manage.py runserver
SECRET_KEY = "WJNDKANJFLWNA420*^$#*@^&%*#^(@$^&!^(*^$(8932946289328915689358)))"

DEBUG = False

# This is just a default value for testing
# Do not include 127.0.0.1 or localhost
# in production for security reasons.
ALLOWED_HOSTS = [
    '127.0.0.1',
    'closedverse.termy.lol',
]

# Test app
#INSTALLED_APPS += 'silk'

#MIDDLEWARE += 'silk.Middleware.SilkyMiddleware'

# Database definition
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/ubuntu/closedverse/my.cnf',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'xff.middleware.XForwardedForMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'closedverse_main.middleware.ClosedMiddleware',
]

XFF_TRUSTED_PROXY_DEPTH = 1
XFF_STRICT = True
XFF_NO_SPOOFING = True
XFF_ALWAYS_PROXY = True
XFF_HEADER_REQUIRED = True

TIME_ZONE = 'EST'

