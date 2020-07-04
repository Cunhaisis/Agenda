from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('display', 'data_evento', 'data_criacao')

admin.site.register(Evento)