from django.db import models

# Create your models here.

# Modelo Página "Sobre Mim" e "Home"

class InfoPessoal(models.Model):
    nome_completo = models.CharField(max_length=100)
    titulo_profissional = models.CharField(max_length=150)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    resumo_longo = models.TextField()
    resumo_curto = models.CharField(max_length=250)
    email_contato = models.EmailField()
    telefone_contato = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    cv_pdf = models.FileField(upload_to='curriculos/', blank=True, null=True, help_text='Faça o upload do seu CV em PDF.')

    class Meta:
        verbose_name = 'Informação Pessoal'
        verbose_name_plural = 'Informações Pessoais'

    def __str__(self):
        return self.nome_completo

# Modelo Experiências Profissionais

class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(help_text='Liste responsabilidades em conquistas em tópicos.')

    class Meta:
        verbose_name = "Experiência Profissional"
        verbose_name_plural = "Experiências Profissionais"
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.cargo} na {self.empresa}"

# Modelo Portfólio

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, help_text='Um identificador único para a URL do projeto.')
    descricao_curta = models.CharField(max_length=250)
    descricao_longa = models.TextField()
    tecnologias_usadas = models.CharField(max_length=200)
    link_projeto = models.URLField(blank=True, null=True, help_text='Link para o projeto online.')
    link_github = models.URLField(blank=True, null=True, help_text='Link para o repositório GitHub')
    imagem_principal = models.ImageField(upload_to='projetos_imagens/', blank=True, null=True)
    data_criacao = models.DateField()

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo

# Modelo Skills

class Habilidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=50, choices=[
        ('linguagem', 'Linguagem de Programação'),
        ('framework', 'Framework/Biblioteca'),
        ('banco_de_dados', 'Banco de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('metodologia', 'Metodologia'),
        ('soft_skill', 'Soft Skill'),
    ])
    nivel_de_conhecimento = models.CharField(max_length=50, blank=True, help_text='Avançado, Intermediário, Básico')

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
        ordering = ['tipo', 'nome']

    def __str__(self):
        return self.nome

# Modelo Formação Acadêmica

class Formacao(models.Model):
    curso = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True, help_text='Detalhes sobre o curso')

    class Meta:
        verbose_name = "Formação Acadêmica"
        verbose_name_plural = "Formações Acadêmicas"
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.curso} em {self.instituicao}"

# Modelo Certificados

class Certificado(models.Model):
    nome_certificacao = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=100)
    ano_conclusao = models.IntegerField()
    link_credencial = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"
        ordering = ['-ano_conclusao']

    def __str__(self):
        return self.nome_certificacao
