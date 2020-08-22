SECRET_KEY = '7(gcmew&obd(773ce(7y_*bp4%1m1bnrb+r@v-ncr9kw@%-z$j'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'noparallel',
]

ROOT_URLCONF = 'noparallel.urls'
WSGI_APPLICATION = 'noparallel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True