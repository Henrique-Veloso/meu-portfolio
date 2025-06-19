from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mim/', views.sobre_mim, name='sobre_mim'),
    path('portfolio/', views.lista_projetos, name='lista_projetos'),
    path('portfolio/<slug:slug>/', views.detalhe_projeto, name='detalhe_projeto'),
    path('contato/', views.contato, name='contato'),
]