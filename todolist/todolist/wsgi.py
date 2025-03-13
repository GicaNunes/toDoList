import os
from django.core.wsgi import get_wsgi_application

# Certifique-se de substituir 'todolist' pelo nome correto do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

application = get_wsgi_application()
