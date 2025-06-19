from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import InfoPessoal, Experiencia, Projeto, Habilidade, Formacao, Certificado
from .forms import ContatoForm

# Create your views here.

# Home
def home(request):
    info_pessoal = InfoPessoal.objects.first()
    projetos_destaque = Projeto.objects.all().order_by('-data_criacao')[:3]

    context = {
        'info_pessoal': info_pessoal,
        'projetos_destaque': projetos_destaque,
    }
    return render(request, 'portfolio/home.html', context)

# Sobre Mim
def sobre_mim(request):
    info_pessoal = InfoPessoal.objects.first()
    experiencias = Experiencia.objects.all()
    formacoes = Formacao.objects.all()
    certificados = Certificado.objects.all()
    habilidades = Habilidade.objects.all()

    context = {
        'info_pessoal': info_pessoal,
        'experiencias': experiencias,
        'formacoes': formacoes,
        'certificados': certificados,
        'habilidades': habilidades,
    }
    return render(request, 'portfolio/sobre_mim.html', context)

# Lista de Projetos
def lista_projetos(request):
    projetos = Projeto.objects.all().order_by('-data_criacao')
    info_pessoal = InfoPessoal.objects.first()

    context = {
        'projetos': projetos,
        'info_pessoal': info_pessoal
    }
    return render(request, 'portfolio/lista_projetos.html', context)

# Detalhes Projeto
def detalhe_projeto(request, slug):
    projeto = get_object_or_404(Projeto, slug=slug)
    info_pessoal = InfoPessoal.objects.first()

    context = {
        'projeto': projeto,
        'info_pessoal': info_pessoal,
    }
    return render(request, 'portfolio/detalhe_projeto.html', context)

# Contato
def contato(request):
    info_pessoal = InfoPessoal.objects.first()
    form = ContatoForm()
    mensagem_sucesso = None

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email_remetente = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            corpo_email = f"Nome: {nome}\n" \
                            f"Email: {email_remetente}\n" \
                            f"Assunto: {assunto}\n\n" \
                            f"Mensagem: \n{mensagem}"
            try:
                send_mail(
                    f"Contato do Site Currículo: {assunto}",
                    corpo_email,
                    settings.EMAIL_HOST_USER,
                    [info_pessoal.email_contato],
                    fail_silently=False,
                )
                mensagem_sucesso = 'Sua mensagem foi enviada com sucesso! Em breve entrarei em contato.'
                form = ContatoForm() 
            except Exception as e:
                mensagem_sucesso = f'Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde. Erro: {e}'
        else:
            mensagem_sucesso = 'Por favor, corrija os erros no formulário.'
    else: 
        form = ContatoForm()
        
    context = {
        'info_pessoal': info_pessoal,
        'form': form,
        'mensagem_sucesso': mensagem_sucesso,
    }
    return render(request, 'portfolio/contato.html', context)