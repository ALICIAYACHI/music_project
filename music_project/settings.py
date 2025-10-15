"""
Django settings for music_project project.
Configurado para funcionar localmente (MySQL) y en Render (PostgreSQL).
"""

from pathlib import Path
import os
import dj_database_url  # para producción en Render

# -----------------------------
# RUTAS BASE
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SEGURIDAD Y CONFIGURACIÓN GENERAL
# -----------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temporal')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'music-project-u5u6.onrender.com',  # tu dominio en Render
    '.onrender.com'
]
CSRF_TRUSTED_ORIGINS = [
    'https://music-project-u5u6.onrender.com',
    'https://*.onrender.com'
]

# -----------------------------
# APLICACIONES INSTALADAS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'music',  # tu app principal
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # para archivos estáticos en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URLS / WSGI
# -----------------------------
ROOT_URLCONF = 'music_project.urls'
WSGI_APPLICATION = 'music_project.wsgi.application'

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta de plantillas global
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

# -----------------------------
# BASE DE DATOS
# -----------------------------
# Si Render define DATABASE_URL, usamos PostgreSQL. Si no, usamos MySQL local.
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'music_db',
            'USER': 'root',
            'PASSWORD': 'admin123',
            'HOST': 'localhost',
            'PORT': '3307',
        }
    }

# -----------------------------
# VALIDADORES DE CONTRASEÑAS
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# INTERNACIONALIZACIÓN
# -----------------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# -----------------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
