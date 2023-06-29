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
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = "stripped"

DEBUG = False

# This is just a default value for testing
# Do not include 127.0.0.1 or localhost
# in production for security reasons.
ALLOWED_HOSTS = [
    '127.0.0.1',
    'closedverse.termy.lol',
]

STATIC_URL = 'https://cimages.termy.lol/'
MEDIA_URL = 'https://cmedia.termy.lol/'
CLOSEDVERSE_PROD = True
#IPHUB_KEY = ""
#DISALLOW_PROXY = True

memo_title = 'Closedverse'
memo_msg = """
<h2>Who?</h2>
this time by term greabaegrjlesnjtsrtlj
<h2>OMFG stop it with the clones</h2>
no
<h2>can i hack this please</h2>
please do not
<h2>what about closedverse-le</h2>
its REALLLLY buggy but if you want to see it on the off chance it hasnt shit itself yet <a href="https://testyy.termy.lol">here</a>
<h2>thank you for this</h2>
you're not welcome this shouldnt exist in the first place
<h2>Shouldn't you be working on rverse?</h2>
dont have access to the computer that i use to work on it lol sorry
"""
IMAGE_DELETE_SETTING = 2

# Test app
#INSTALLED_APPS += 'silk'

#MIDDLEWARE += 'silk.Middleware.SilkyMiddleware'
#MIDDLEWARE.append('x_forwarded_for.middleware.XForwardedForMiddleware')

# Database definition
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/ubuntu/closedverse/my.cnf',
        }
    }
}"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'closedverse.sqlite3'),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'xff.middleware.XForwardedForMiddleware',
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

