from django.contrib import admin
from .models import Inf, Acesso

# Registrar Inf normalmente
admin.site.register(Inf)


@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ['ip', 'caminho', 'data_acesso']
    list_filter = ['data_acesso', 'caminho']
    search_fields = ['ip', 'caminho']
    readonly_fields = ['ip', 'caminho', 'data_acesso']
    ordering = ['-data_acesso']

    # adiciona a action
    @admin.action(description="DELETE ALL  Acessos")
    def apagar_todos_acessos(self, request, queryset):
        Acesso.objects.all().delete()

    actions = [apagar_todos_acessos]
