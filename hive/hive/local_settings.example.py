import os
PROJECT_ROOT = os.path.dirname(os.path.dirname( os.path.realpath(__file__)))

DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'astin@iz4u.net'
EMAIL_HOST_PASSWORD = '1234qwer'
EMAIL_PORT = 587

if os.environ.has_key("PRODUCTION"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else: # DEVELOPMENT
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'hive.sq3',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media/")
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+'/static/'
STATIC_URL = '/static/'

SECRET_KEY = '9%uc#6x6yk!ri07guig#i2_8kns9y%wdgrqrw8&amp;z4phcgq!*a!'

#django celery
BROKER_URL = 'django://'

