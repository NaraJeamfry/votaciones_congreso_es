# Generated by Django 3.0.3 on 2022-02-25 03:41

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_grupoparlamentario_congresos'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoparlamentario',
            name='color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None),
        ),
    ]
