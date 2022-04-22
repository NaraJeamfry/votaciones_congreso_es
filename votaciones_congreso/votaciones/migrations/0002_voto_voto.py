# Generated by Django 3.0.3 on 2022-02-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voto',
            name='voto',
            field=models.CharField(choices=[('favor', 'A favor'), ('contra', 'En contra'), ('abst', 'Abstención')], default=None, max_length=10, verbose_name='Contenido del voto'),
            preserve_default=False,
        ),
    ]