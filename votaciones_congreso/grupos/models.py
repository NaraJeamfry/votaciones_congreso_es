from colorfield.fields import ColorField
from django.db import models


class GrupoParlamentario(models.Model):
    nombre = models.CharField(max_length=200)
    congresos = models.ManyToManyField('congreso.Congreso', related_name='grupos_parlamentarios')
    partidos = models.ManyToManyField('grupos.PartidoPolitico', related_name='grupos_parlamentarios')
    color = ColorField(default='#000000')

    def __str__(self):
        return f'{self.nombre}'


class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'
