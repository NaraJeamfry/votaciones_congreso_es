from django.contrib import admin

from congreso.models import Legislatura, Congreso, AsientosCongreso, CircunscripcionElectoral, Hemiciclo
from diputados.admin import ActaDiputadoInline


@admin.register(Legislatura)
class LegislaturaAdmin(admin.ModelAdmin):
    pass


class AsientoCongresoInline(admin.StackedInline):
    model = AsientosCongreso


@admin.register(Congreso)
class CongresoAdmin(admin.ModelAdmin):
    inlines = [
        AsientoCongresoInline,
    ]


@admin.register(CircunscripcionElectoral)
class CircunscripcionElectoralAdmin(admin.ModelAdmin):
    pass


@admin.register(Hemiciclo)
class HemicicloAdmin(admin.ModelAdmin):
    inlines = [
        ActaDiputadoInline,
    ]


