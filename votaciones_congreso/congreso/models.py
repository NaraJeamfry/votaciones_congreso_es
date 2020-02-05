from django.db import models


class Provincia(models.Model):
    nombre = models.CharField(max_length=32)
    habitantes = models.IntegerField()
    escanos = models.IntegerField()
