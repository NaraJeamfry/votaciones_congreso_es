from django.db import models


class GrupoParlamentario(models.Model):
    nombre = models.CharField(max_length=200)
