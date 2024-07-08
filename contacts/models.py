from django.db import models
from django.utils import timezone

class Contact(models.Model):
    Primeiro_nome = models.CharField(max_length=50)
    segundo_nome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    Data_atual = models.DateTimeField(default=timezone.now)
    complemento = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.Primeiro_nome} {self.segundo_nome}'
