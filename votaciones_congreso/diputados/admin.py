from django.contrib import admin

from diputados.models import Diputado, ActaDiputado


class ActaDiputadoInline(admin.StackedInline):
    model = ActaDiputado


@admin.register(Diputado)
class DiputadoAdmin(admin.ModelAdmin):
    inlines = [
        ActaDiputadoInline,
    ]
    exclude = ('hemiciclos',)
