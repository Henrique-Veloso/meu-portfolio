from django.contrib import admin
from .models import InfoPessoal, Experiencia, Projeto, Habilidade, Formacao, Certificado

# Register your models here.

admin.site.register(InfoPessoal)
admin.site.register(Experiencia)
admin.site.register(Projeto)
admin.site.register(Habilidade)
admin.site.register(Formacao)
admin.site.register(Certificado)
