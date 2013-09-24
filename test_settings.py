# -*- coding: utf-8 -*-

SECRET_KEY = 'psst'
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ROOT_URLCONF = 'allauth.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.dropbox_provider',
    'allauth.socialaccount.providers.facebook_provider',
    'allauth.socialaccount.providers.google_provider',
    'allauth.socialaccount.providers.github_provider',
    'allauth.socialaccount.providers.linkedin_provider',
    'allauth.socialaccount.providers.openid_provider',
    'allauth.socialaccount.providers.persona_provider',
    'allauth.socialaccount.providers.soundcloud_provider',
    'allauth.socialaccount.providers.stackexchange_provider',
    'allauth.socialaccount.providers.twitch_provider',
    'allauth.socialaccount.providers.twitter_provider',
    'allauth.socialaccount.providers.vimeo_provider',
    'allauth.socialaccount.providers.weibo_provider',
    'allauth.socialaccount.providers.bitly_provider',
    'allauth.socialaccount.providers.vk_provider',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

STATIC_URL = '/static/'
