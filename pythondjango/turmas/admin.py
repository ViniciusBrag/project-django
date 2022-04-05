from calendar import c
from django.contrib import admin
from pythondjango.turmas.models import Turmas


class MatriculaInline(admin.TabularInline):
    model = Turmas.alunos.through
    extra = 1
    redonly_fields = ('data',)
    autocomplete_fields = ('usuario', )
    ordering = ('-data',)

@admin.register(Turmas)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome', )}
    ordering = ('-inicio',)

