
import logging
from django.utils.deprecation import MiddlewareMixin
from django.db import DatabaseError
from .models import Acesso

logger = logging.getLogger(__name__)


class AcessoMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = self.get_client_ip(request)
        caminho = request.path

        try:
            Acesso.objects.create(
                ip=ip,
                caminho=caminho
            )
        except DatabaseError:
            logger.exception(
                "Não foi possível registar o acesso."
            )

        return None

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get(
            'HTTP_X_FORWARDED_FOR'
        )

        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()

        return request.META.get('REMOTE_ADDR')
