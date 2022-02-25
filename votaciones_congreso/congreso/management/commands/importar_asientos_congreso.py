import argparse
import json

from django.core.management.base import BaseCommand, CommandError

from congreso.models import AsientosCongreso, Congreso


class Command(BaseCommand):
    help = 'Importa un JSON con info sobre los asientos de un congreso.'

    def add_arguments(self, parser):
        parser.add_argument('id_congreso', type=int)
        parser.add_argument('json_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        id_congreso = options['id_congreso']
        json_file = options['json_file']

        try:
            congreso = Congreso.objects.get(id=id_congreso)
        except Congreso.DoesNotExist:
            raise CommandError('Este congreso no existe!')

        asientos = json.load(json_file)
        congreso.asientos.all().delete()

        for asiento in asientos:
            new_asiento = AsientosCongreso(congreso=congreso, num_asiento=asiento['numero'],
                                           posicion_x=asiento['x'], posicion_y=asiento['y'])
            new_asiento.save()

