from django.db import models

class Inf(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.titulo
        
class Acesso(models.Model):
    ip = models.GenericIPAddressField()
    caminho = models.CharField(max_length=255)  # URL acessada
    data_acesso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip} - {self.caminho} - {self.data_acesso.strftime('%d/%m/%Y %H:%M')}"        
        
               
