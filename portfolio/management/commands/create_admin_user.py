import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand): 
    help = 'Cria um superusuário no ambiente online se não existir, usando variáveis de ambiente.'

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write(self.style.WARNING('Variáveis de ambiente DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD não estão definidas. Pulando a criação do superusuário.'))
            return

        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_superuser(username, email, password)
                self.stdout.write(self.style.SUCCESS(f'Superusuário "{username}" criado com sucesso.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erro ao criar superusuário: {e}'))
        else:
            self.stdout.write(self.style.WARNING(f'Superusuário "{username}" já existe.'))