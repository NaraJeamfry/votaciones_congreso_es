from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _


class CircunscripcionElectoral(models.Model):
    nombre = models.CharField(_('Nombre de la circunscripción'), max_length=32)
    habitantes = models.IntegerField(_('Número de habitantes'))
    escanos = models.IntegerField(_('Número de escaños'))

    class Meta:
        verbose_name = _('Circunscripción Electoral')
        verbose_name_plural = _('Circunscripciones Electorales')

    def __str__(self):
        return f'{self.nombre}'


class Legislatura(models.Model):
    nombre = models.CharField(_('Nombre de la Legislatura'), max_length=32)
    inicio = models.DateField(_('Fecha de inicio'))
    fin = models.DateField(_('Fecha de cierre'), null=True, blank=True)  # Si es None, legislatura actual

    class Meta:
        verbose_name = _('Legislatura')
        verbose_name_plural = _('Legislaturas')

    def __str__(self):
        if self.fin:
            return f'{self.nombre} ({self.inicio.year}-{self.fin.year})'
        else:
            return f'{self.nombre} (Actual)'


class Congreso(models.Model):
    legislatura = models.OneToOneField('congreso.Legislatura', on_delete=models.CASCADE, related_name='congreso')

    ancho_imagen_hemiciclo = models.IntegerField(_('Ancho de imagen hemiciclo'), null=True, blank=True)
    alto_imagen_hemiciclo = models.IntegerField(_('Alto de imagen hemiciclo'), null=True, blank=True)
    radio_circulo_hemiciclo = models.IntegerField(_('Radio de círculos hemiciclo'), null=True, blank=True)

    bg_hemiciclo = models.ImageField(_('Fondo imagen hemiciclo'), null=True, blank=True)

    @property
    def ultimo_hemiciclo(self):
        if self.hemiciclos.filter(fin__isnull=True).count() > 0:
            return self.hemiciclos.filter(fin__isnull=True).first()
        elif self.hemiciclos.count() > 0:
            return self.hemiciclos.order_by('-fin').first()
        else:
            return None

    def __str__(self):
        return f'Congreso de la {self.legislatura}'


class AsientosCongreso(models.Model):
    congreso = models.ForeignKey('congreso.Congreso', on_delete=models.CASCADE, related_name='asientos')

    num_asiento = models.IntegerField(_('Número asiento'))

    posicion_x = models.IntegerField(_('Posición en el eje X'), null=True, blank=True)
    posicion_y = models.IntegerField(_('Posición en el eje Y'), null=True, blank=True)

    @property
    def color_ultimo_hemiciclo(self):
        hemiciclo = self.congreso.ultimo_hemiciclo
        if hemiciclo and hemiciclo.asiento_ocupado(self.num_asiento):
            return hemiciclo.grupo_parlamentario_en(self.num_asiento).color
        return '#000000'

    class Meta:
        unique_together = ('congreso', 'num_asiento')

    def __str__(self):
        return f'Asiento {self.num_asiento} del {self.congreso}'


class Hemiciclo(models.Model):
    inicio = models.DateField(_('Fecha de inicio'))
    fin = models.DateField(_('Fecha de fin'), null=True)  # Si es None, hemiciclo actual
    congreso = models.ForeignKey('congreso.Congreso', on_delete=models.CASCADE, related_name='hemiciclos')

    def asiento_ocupado(self, num_asiento: int) -> bool:
        acta_asiento = self.diputados.filter(actadiputado__asiento__num_asiento=num_asiento)
        return acta_asiento.exists()

    def diputado_en(self, num_asiento: int) -> Optional['Diputado']:
        diputados = self.diputados.filter(actadiputado__asiento__num_asiento=num_asiento)
        if diputados.exists():
            return diputados.first()
        return None

    def grupo_parlamentario_en(self, num_asiento: int) -> Optional['GrupoParlamentario']:
        acta_asientos = self.actadiputado_set.filter(asiento__num_asiento=num_asiento)
        if acta_asientos.exists():
            return acta_asientos.first().grupo_parlamentario
        return None

    def __str__(self):
        return f'Integrantes del Congreso de la {self.congreso.legislatura.nombre} ({self.inicio} - {self.fin})'
