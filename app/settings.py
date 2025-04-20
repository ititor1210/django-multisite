from pathlib import Path
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティ
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key_for_local')  # 本番用のSECRET_KEYは環境変数で設定
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['django-multisite.onrender.com', 'localhost', '127.0.0.1']

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookstore',
    'stats',
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

# データベース
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'multisite_db'),
        'USER': os.getenv('DB_USER', 'multisite_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', '5xdhKDHuCzKLZ4v4SIGsRvgH4Mm2SrAm'),
        'HOST': os.getenv('DB_HOST', 'dpg-d01u5iidbo4c7394sddg-a.singapore-postgres.render.com'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# パスワード検証
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

# 言語設定
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 静的ファイル
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# デフォルトの主キー
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
