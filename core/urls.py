from django.urls import path
from .views import LinkView, Link1, CadastroView, CreateLinkView



urlpatterns = [
    path('projeto/', LinkView.as_view(), name='projeto'),
    path('projeto_pronto/', Link1, name='projeto_pronto'),
    path('cadastro_usuario/', CadastroView.as_view(), name='cadastro'),
    path('criando_tela/', CreateLinkView.as_view(), name='criando_tela'),

]