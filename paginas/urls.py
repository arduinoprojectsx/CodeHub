from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import InfoListView, Index, Sobre, Servicos, Contato, Termos, Privacidade, Jogos, Click, Guess, Feedback, Memory, Cookies


from django.http import FileResponse
import os

urlpatterns = [
    path('info/', InfoListView.as_view(), name='info'),
    path('', Index.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('services/', Servicos, name='servicos'),
    path('contato/', Contato.as_view(), name='contato'),
    path('feedback/', Feedback    , name='feedback'),
    path('cookies/', Cookies.as_view(), name='cookies'),

    # Novas páginas obrigatórias para AdSense
    path('termos/', Termos.as_view(), name='termos'),
    path('privacidade/', Privacidade.as_view(), name='privacidade'),
    

    path('jogos/', Jogos.as_view(), name='jogos'),
    path('jogos/click', Click.as_view(), name='click'),
    path('jogos/guess', Guess.as_view(), name='guess'),
    path('jogos/memory', Memory.as_view(), name='memory'),

    # Arquivo ads.txt
    path("ads.txt", lambda request: FileResponse(open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "ads.txt"), "rb"
    ))),

    path("sitemap.xml", lambda request: FileResponse(open("static/sitemap.xml", "rb"))),
    
    path("robots.txt", lambda request: FileResponse(open("static/robots.txt", "rb"))),

    path("logo", lambda request: FileResponse(
    open(os.path.join(settings.BASE_DIR, "static", "img", "logo.png"), "rb"),
    content_type="image/png"
), name="logo"),

    
]

# Arquivos estáticos (modo desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
