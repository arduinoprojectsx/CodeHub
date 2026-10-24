from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Inf
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

# Páginas estáticas
class Index(TemplateView):
    template_name = 'paginas/index.html'

class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'

class Contato(TemplateView):
    template_name = 'paginas/contacto.html'

class Termos(TemplateView):
    template_name = 'paginas/termos.html'

class Privacidade(TemplateView):
    template_name = 'paginas/privacidade.html'
    
class Cookies(TemplateView):
    template_name='paginas/cookies.html' 

class Click(TemplateView):
    template_name='paginas/click.html'

class Guess(TemplateView):
    template_name='paginas/guess.html'
    
class Memory(TemplateView):
    template_name='paginas/memory.html' 
    
class Jogos(TemplateView):
    template_name='paginas/jogos.html'

# Info
class InfoCreateView(CreateView):
    model = Inf
    fields = ['titulo', 'descricao', 'imagem']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('info')

class InfoListView(ListView):
    model = Inf
    template_name = 'paginas/info.html'
    context_object_name = 'itens'

# Serviços com envio de e-mail
def Servicos(request):
    enviado = False
    erro = False

    if request.method == "POST":
        tipo = request.POST.get('tipo')
        email_cliente = request.POST.get('email_cliente')
        mensagem = request.POST.get('mensagem')

        corpo_email = f"""
        Novo pedido de serviço:

        Tipo de Serviço: {tipo}
        E-mail do Cliente: {email_cliente}
        Descrição do Projeto:
        {mensagem}
        """

        try:
            send_mail(
                subject='Novo Pedido de Serviço',
                message=corpo_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['nevesjosemar9@gmail.com'],
                fail_silently=False,
            )
            enviado = True
        except Exception as e:
            print("Erro ao enviar email:", e)
            erro = True

    return render(request, 'paginas/servicos.html', {'enviado': enviado, 'erro': erro})
    
def Feedback(request):
    enviado = False
    erro = False

    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        corpo_email = f"""
        Novo feedback recebido:

        Nome: {nome}
        E-mail: {email}
        Mensagem:
        {mensagem}
        """

        try:
            send_mail(
                subject='Novo Feedback do Site',
                message=corpo_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['nevesjosemar9@gmail.com'],
                fail_silently=False,
            )
            enviado = True
        except Exception as e:
            print("Erro ao enviar feedback:", e)
            erro = True

    return render(request, 'paginas/feedback.html', {'enviado': enviado, 'erro': erro})