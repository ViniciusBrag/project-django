from calendar import c
from django.contrib import admin
from pythondjango.turmas.models import Turmas

@admin.register(Turmas)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome', )}
    ordering = ('-inicio',)

