from django.contrib import admin
from contacts import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

