from django.db import models
from django.utils import timezone

class Category(models.Model):
    Nome = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.Nome 

class Contact(models.Model):
    Primeiro_nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50, blank = True)
    telefone = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254, blank = True)
    Data_atual = models.DateTimeField(default = timezone.now)
    complemento = models.TextField(blank = True)
    show = models.BooleanField(default = True)
    pictures = models.ImageField(blank = True, upload_to = 'pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self) -> str:
        return f'{self.Primeiro_nome} {self.sobrenome}'
    

