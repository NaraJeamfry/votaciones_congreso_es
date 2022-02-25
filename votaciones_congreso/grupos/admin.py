from django.contrib import admin

from grupos.models import PartidoPolitico, GrupoParlamentario


@admin.register(PartidoPolitico)
class PartidoPoliticoAdmin(admin.ModelAdmin):
    pass


@admin.register(GrupoParlamentario)
class GrupoParlamentarioAdmin(admin.ModelAdmin):
    pass
