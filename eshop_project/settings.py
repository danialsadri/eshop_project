from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9qts1=s)$ky8o%%_$_#j#dmb106oas2_-n6shcfp$yg2g@uxny'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOCAL_APPS = [
    'account_module.apps.AccountModuleConfig',
    'home_module.apps.HomeModuleConfig',
    'product_module.apps.ProductModuleConfig',
    'contact_module.apps.ContactModuleConfig',
    'site_module.apps.SiteModuleConfig',
    'article_module.apps.ArticleModuleConfig',
    'user_panel_module.apps.UserPanelModuleConfig',
    'order_module.apps.OrderModuleConfig',
    'polls.apps.PollsConfig',
]

THIRD_PARTY_APPS = [
    'django_render_partial',
    'sorl.thumbnail',
    'jalali_date',
    'widget_tweaks',
]

INSTALLED_APPS = [
    'admin_persian',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *LOCAL_APPS,
    *THIRD_PARTY_APPS,
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin_panel/js/django_jalali.min.js',
            # OR
            # 'admin_panel/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin_panel/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin_panel/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin_panel/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin_panel/js/main.js',
        ],
        'css': {
            'all': [
                'admin_panel/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'warning.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
        },
    },
}

LANGUAGE_CODE = 'fa-IR'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'staticfiles']
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ROOT_URLCONF = 'eshop_project.urls'
WSGI_APPLICATION = 'eshop_project.wsgi.application'

AUTH_USER_MODEL = 'account_module.User'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
EMAIL_PORT = 587

MERCHANT = '***'
ZP_API_REQUEST = 'https://api.zarinpal.com/pg/v4/payment/request.json'
ZP_API_VERIFY = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
ZP_API_STARTPAY = 'https://www.zarinpal.com/pg/StartPay/{authority}'
description = 'نهایی کردن خرید شما از سایت ما'
CallbackURL = 'http://127.0.0.1:8000/orders/verify-payment/'
