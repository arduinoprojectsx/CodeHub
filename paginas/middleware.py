from django.utils.deprecation import MiddlewareMixin
from datetime import timedelta
from django.utils import timezone
from .models import Acesso

class AcessoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = self.get_client_ip(request)
        caminho = request.path

        Acesso.objects.create(ip=ip, caminho=caminho)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
