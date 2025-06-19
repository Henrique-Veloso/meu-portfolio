import os
import django
from django.conf import settings
from django.contrib.auth.models import User

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not all([username, email, password]):
    print("Erro: Variáveis de ambiente DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD não estão definidas. A criação do superusuário falhou.")
else:
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superusuário '{username}' criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar superusuário: {e}")
    else:
        print(f"Superusuário '{username}' já existe.")