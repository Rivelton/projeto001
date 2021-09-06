from django.shortcuts import render

from django.views.generic import FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Link, CustomUsuario
from .forms import LinkModelForm, CustomUsuarioCreateForm
from django.urls import reverse_lazy


class CadastroView(FormView):

    template_name = 'cadastro.html'
    form_class = CustomUsuarioCreateForm
    success_url = reverse_lazy('index')





class LinkView(ListView):
    models = Link
    template_name = 'lista_projeto.html'
    queryset = Link.objects.all()
    context_object_name = 'link'


class CreateLinkView(CreateView):
    models = Link
    template_name = 'criando_tela.html'
    fields = ['nome', 'nickname', 'descricao', 'link', 'icone', 'imagem']
    success_url = reverse_lazy('projeto')
    queryset = Link.objects.all()



def Link1(request):
    form = LinkModelForm()
    context = {
            'form': form
    }
    return render(request, 'projeto_pronto.html', context)
