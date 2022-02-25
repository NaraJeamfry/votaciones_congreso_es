from django.db import models
from django.utils.translation import gettext_lazy as _


class Sesion(models.Model):
    numero_sesion = models.IntegerField(_('Número de sesión'))
    fecha = models.DateField(_('Fecha de la sesión'))

    congreso = models.ForeignKey('congreso.Congreso', on_delete=models.CASCADE, related_name='sesiones')


class Votacion(models.Model):
    class Resultados(models.TextChoices):
        SI = 'Si', _('Sí')
        NO = 'No', _('No')

    numero_votacion = models.IntegerField(_('Posición'))
    sesion = models.ForeignKey('votaciones.Sesion', on_delete=models.CASCADE, related_name='votaciones')

    resultado = models.CharField(_('Resultado de la votación'), choices=Resultados.choices, max_length=8, null=False, blank=False)
    presentes = models.IntegerField(_('Recuento de presentes'))
    favor = models.IntegerField(_('Recuento de votos a favor'))
    contra = models.IntegerField(_('Recuento de votos en contra'))
    abstenciones = models.IntegerField(_('Recuento de abstenciones'))
    no_votan = models.IntegerField(_('Recuento de no-votos'))


class Voto(models.Model):
    class Tipo(models.TextChoices):
        FAVOR = 'favor', _('A favor')
        CONTRA = 'contra', _('En contra')
        ABSTENCION = 'abst', _('Abstención')

    votacion = models.ForeignKey('votaciones.Votacion', on_delete=models.CASCADE, related_name='votos')
    diputado = models.ForeignKey('diputados.ActaDiputado', on_delete=models.SET_NULL, related_name='votos', null=True)
    voto = models.CharField(_('Contenido del voto'), choices=Tipo.choices, max_length=10)


