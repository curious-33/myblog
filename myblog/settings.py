from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD:myblog/settings.py
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
=======
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
SECRET_KEY = '56%pn5nyem^-!kpl^3wxf2@4h(m=)&4jjt8c_dicd-vo&)k)0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

<<<<<<< HEAD:myblog/settings.py
# Application definition

=======
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd part libraries
    'rest_framework',
    'rest_framework.authtoken',
    'tinymce',

    # our apps
    'user.apps.UserConfig',
    'blog.apps.BlogConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'
<<<<<<< HEAD:myblog/settings.py

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
=======
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

<<<<<<< HEAD:myblog/settings.py
        'PASSWORD': 'curious',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

=======
        'NAME': os.path.join(BASE_DIR,'blog.sqlite3',)
    }
}

>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
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

<<<<<<< HEAD:myblog/settings.py
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

=======
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False
<<<<<<< HEAD:myblog/settings.py
=======

>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py

AUTH_USER_MODEL = 'user.User'

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
<<<<<<< HEAD:myblog/settings.py
        'rest_framework.authentication.BasicAuthentication',
=======
        'rest_framework.authentication.SessionAuthentication',
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DATETIME_FORMAT': "%Y-%m-%d - %H:%M:%S",
}
<<<<<<< HEAD:myblog/settings.py
=======

TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "path/to/tiny_mce")
>>>>>>> origin/rasulovmuxtor:blog/blog/settings.py
