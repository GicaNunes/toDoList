from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Mantenha a chave secreta segura utilizando variáveis de ambiente
SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-de-desenvolvimento')

DEBUG = True
ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com']

# Página para onde o usuário será redirecionado após fazer login com sucesso
LOGIN_REDIRECT_URL = '/'  # Redireciona para a página inicial (ou outra URL desejada)

# Página para onde o usuário será redirecionado após fazer logout
LOGOUT_REDIRECT_URL = '/'  # Redireciona para a página inicial (ou outra URL desejada)



# Domínios/hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    # Aplicações padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Sua aplicação personalizada
    'tasks',  # Certifique-se de que o nome é o correto
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Adicionada para gerenciar sessões
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Adicionada para autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Adicionada para mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Adicione o diretório dos seus templates, se necessário
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

WSGI_APPLICATION = 'todolist.wsgi.application'

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

# Configurações de idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Diretório contendo arquivos estáticos originais
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório para o comando collectstatic


# Configuração da chave primária padrão para novos modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
