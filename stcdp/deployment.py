import os
from .settings import *
from urllib.parse import urlparse



# Allowed Hosts and CSRF
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]

# Security
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']


CORS_ALLOWED_ORIGINS = [
    'https://thankful-plant-070054403.5.azurestaticapps.net'
]


# Middleware Configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_auth_adfs.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Static Files Storage
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Database Configuration
CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']



url = urlparse(CONNECTION)

# Extract the necessary parts
CONNECTION_STR = {
    'dbname': url.path[1:],
    'host': url.hostname,
    'user': url.username,
    'password': url.password,
    'port': url.port
}

# Set up Django's DATABASES setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONNECTION_STR['dbname'],
        'HOST': CONNECTION_STR['host'],
        'USER': CONNECTION_STR['user'],
        'PASSWORD': CONNECTION_STR['password'],
        'PORT': CONNECTION_STR.get('port', '5432'),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = 'default from email'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / 'staticfiles'
AZURE_REDIRECT_URI=os.environ['AZURE_REDIR_URI']

AUTH_ADFS = {
    'AUDIENCE': os.environ['API_IDENTIFIER'],
    'CLIENT_ID': os.environ['AZURE_CLIENT_ID'],
    'CLIENT_SECRET': os.environ['AZURE_CLIENT_SECRET'],
    'TENANT_ID': os.environ['AZURE_TENANT_ID'],
    'RELYING_PARTY_ID': os.environ['RELYING_PARTY_ID'],
    'LOGIN_EXEMPT_URLS': [
        r'^api/v1/.*$',
        r'^api/v1/users/callback/$',  
    ],
    'CLAIM_MAPPING': {
        'first_name': 'given_name',
        'last_name': 'family_name',
        
    },
    'CA_BUNDLE': True,
}