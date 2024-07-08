from django.contrib import admin
from contacts import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'Primeiro_nome', 'segundo_nome', 'telefone', 'email', 'Data_atual',
    ordering = '-id',
    # list_filter = 'create_date',
    search_fields = 'Primeiro_nome', 'segundo_nome', 'telefone', 'email',
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'Primeiro_nome', 'segundo_nome', 'telefone', 'email',

