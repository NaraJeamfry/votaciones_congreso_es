from django.db import models

from congreso.models import Legislatura


class ActaDiputado(models.Model):
    diputado = models.ForeignKey('diputados.Diputado', on_delete=models.CASCADE)
    hemiciclo = models.ForeignKey('congreso.Hemiciclo', on_delete=models.CASCADE)
    asiento = models.ForeignKey('congreso.AsientosCongreso', on_delete=models.SET_NULL, null=True)
    grupo_parlamentario = models.ForeignKey('grupos.GrupoParlamentario', on_delete=models.SET_NULL, null=True)


class Diputado(models.Model):
    nombre = models.CharField(max_length=120, null=False, blank=False)
    apellidos = models.CharField(max_length=120, null=False, blank=False)

    provincia = models.ForeignKey('congreso.CircunscripcionElectoral',
                                  on_delete=models.CASCADE,
                                  related_name='diputados')
    grupos_parlamentarios = models.ManyToManyField('grupos.GrupoParlamentario',
                                                   related_name='diputados')
    hemiciclos = models.ManyToManyField('congreso.Hemiciclo', through='diputados.ActaDiputado', related_name='diputados')

    nacimiento = models.DateField(null=True, blank=True)

    @property
    def nombre_completo(self):
        return f'{self.apellidos}, {self.nombre}'

    def en_legislatura(self, legislatura: Legislatura) -> bool:
        pass

    def __str__(self):
        return f'{self.nombre_completo} ({self.provincia})'
