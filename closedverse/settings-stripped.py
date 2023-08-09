"""
Django settings for closedverse project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! (If you want a website that can generate key https://miniwebtool.com/django-secret-key-generator/ goto here.)
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This is just a default value for testing
# Do not include 127.0.0.1 or localhost
# in production for security reasons.
ALLOWED_HOSTS = [
    '127.0.0.1',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATIC_URL = '/s/'
MEDIA_URL = '/media/'
CLOSEDVERSE_PROD = True

memo_title = 'closedverse-video-support'
memo_msg = """
<h2>basically the clusterfuck of all closedverse clones</h2>
<p>i don't know what i'm doing</p>
<h2>Why is this person rehosting it?</h2>
<p>the world may never know</p>"""
IMAGE_DELETE_SETTING = 2

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'markdown_deux',
    'closedverse_main',
    #'ban',
    #'maintenance',
]
X_FRAME_OPTIONS='SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # use this middleware if you need x-forwarded-for support
    #'xff.middleware.XForwardedForMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'ban.middleware.BanManagement',
    'closedverse_main.middleware.ClosedMiddleware',
    #'maintenance.middleware.MaintenanceManagement',
]
if not DEBUG:
	MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

ROOT_URLCONF = 'closedverse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'closedverse_main.context_processors.brand_name_universal',
            ],
        },
    },
]

WSGI_APPLICATION = 'closedverse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'closedverse.sqlite3'),
    }
}


"""
# log errors.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
"""


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# replace with your own timezone
TIME_ZONE = 'America/New_York'

# Disable internationalization because Closedverse doesn't use it
USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#STATIC_URL = '/static/'
if not DEBUG:
	# without this, this will not serve static for admin (and other apps potentially)
	WHITENOISE_USE_FINDERS = True
	STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
	STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
else:
	# Define static files in the base directory
	STATICFILES_DIRS = [
	    os.path.join(BASE_DIR, 'static/'),
	]

# Closedverse models and routes for Django
AUTH_USER_MODEL = 'closedverse_main.User'
CSRF_FAILURE_VIEW = 'closedverse_main.views.csrf_fail'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'

# User-uploaded media paths for Closedverse
#MEDIA_URL = '/media/'
# Must end with a trailing slash
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Settings for markdown_deux, a module
# that Closedverse uses in user messages
MARKDOWN_DEUX_STYLES = {
    'default': {
        'extras': {
            'code-friendly': None,
        },
        'safe_mode': 'escape',
    },
}

# Initialize version and Git URL
CLOSEDVERSE_GIT_VERSION = 'unknown'
CLOSEDVERSE_GIT_URL = ''
CLOSEDVERSE_GIT_HAS_CHANGES = False

# Only set git version/URL if .git folder exists
if os.path.isdir(os.path.join(BASE_DIR, '.git')):
    # Get version from Git. This is shown in the layout
    git_process = os.popen('git rev-parse HEAD', 'r')
    CLOSEDVERSE_GIT_VERSION = git_process.read()[:-1]

    # if this command returns a non-zero exit code, then
    # there have been some changes so let's indicate that
    if os.system('git diff-index --quiet HEAD --'):
        CLOSEDVERSE_GIT_HAS_CHANGES = True

    git_process = os.popen('git remote get-url origin', 'r')
    CLOSEDVERSE_GIT_URL = git_process.read()[:-1]

    try:
        git_url_without_ext = CLOSEDVERSE_GIT_URL.split('.git')[0]
    except IndexError:
        pass
    else:
        CLOSEDVERSE_GIT_URL = git_url_without_ext + '/commit/' + CLOSEDVERSE_GIT_VERSION

# Google reCAPTCHA (v2) settings
# This feature won't work if these fields are not populated.
RECAPTCHA_PUBLIC_KEY = None
RECAPTCHA_PRIVATE_KEY = None

# Key for IPHub service for Closedverse, which detects proxies.
IPHUB_KEY = None
# If this is set to True, then users will receive an error
# upon trying to sign up for the site behind a proxy.
# Uses IPHub service and requires an API key defined above.
DISALLOW_PROXY = False

# Setting this to True forces every user to log in/
# sign up for the site to view any content.
FORCE_LOGIN = False
# A list of URLs that are always accessible
# whether the above value is set or not.
LOGIN_EXEMPT_URLS = {
    r'^login/$',
    r'^signup/$',
    r'^logout/$',
    r'^reset/$',
    r'^help/rules$',
    r'^help/contact$',
    r'^help/login$',
}

# Action to perform on images belonging to posts/
# comments when they are deleted
# 0: keep, 1: move to 'rm' folder, 2: delete
IMAGE_DELETE_SETTING = 2

# List of NNIDs that aren't allowed to be used on the site.
#NNID_FORBIDDEN_LIST = os.path.join(BASE_DIR, 'forbidden.json')

# allow sign ups.
allow_signups = True

# Whatever the reason may be, you have the option to make your clone invite only.
invite_only = False

# Minimum level required to view IP addresses and user agents. (default: 10)
# Mods under this level will still be able to manage users, however will not be able to view any sensitive data.
min_lvl_metadata_perms = 100

# if someone's level is equal or above this, they can edit most community on your clone.
level_needed_to_man_communities = 5

# if someone's level is equal or above this, they can edit any user with a lower level on your clone.
level_needed_to_man_users = 5

# file size limits in megabytes! only applies when using the community tools.
max_icon_size = .5
max_banner_size = 1

# The minimum length required for a user's password. This is to save the users from themselves in the event of a data breach. The longer and more complex the password is, the harder it is to be cracked. (default: 7)
# This will definitely miss a few people off who just want to sign up without worrying about long passwords.
minimum_password_length = 7

# The hard limit for uploading, Will cause an error if this is exceeded. This is set to 15MB by default (15728640)
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800

# Set the default theme here! Set this to None to use the normal Closedverse theme.
# TODO, make this work for users who aren't logged in.
site_wide_theme_hex = "#ff00cd"

# Option to delete image if it's local
# 0 - keep, 1 - move to 'rm' folder, 2 - DELETE
image_delete_opt = 0

# age (minimal 13 due to C.O.P.P.A)
age_allowed = "13"

# brand name currently being implemented throughout templates
brand_name = "Closedverse"

# This option enables some production-specific pages
# and routines, such as HTTPS scheme redirection and
# proxy detection via IPHub.
CLOSEDVERSE_PROD = True

XFF_TRUSTED_PROXY_DEPTH = 1
XFF_STRICT = True
XFF_NO_SPOOFING = True
XFF_ALWAYS_PROXY = True
XFF_HEADER_REQUIRED = True

# uncomment this if you want miis to be retrieved on the server
#mii_endpoint = '/origin?a='
