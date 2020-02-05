from django.db import models


class Diputado(models.Model):
    nombre = models.CharField(max_length=120, null=False, blank=False)
    apellidos = models.CharField(max_length=120, null=False, blank=False)

    provincia = models.ForeignKey('congreso.Provincia',
                                  on_delete=models.CASCADE,
                                  related_name='diputados')
    grupo_parlamentario = models.ForeignKey('grupos.GrupoParlamentario',
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='diputados')

    nacimiento = models.DateField(null=True, blank=True)

    @property
    def nombre_completo(self):
        return f'{self.apellidos}, {self.nombre}'

