# Generated by Django 3.0.3 on 2022-02-25 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0005_auto_20220225_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='congreso',
            name='alto_imagen_hemiciclo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Alto de imagen hemiciclo'),
        ),
        migrations.AddField(
            model_name='congreso',
            name='ancho_imagen_hemiciclo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ancho de imagen hemiciclo'),
        ),
        migrations.AddField(
            model_name='congreso',
            name='bg_hemiciclo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Fondo imagen hemiciclo'),
        ),
        migrations.AddField(
            model_name='congreso',
            name='radio_circulo_hemiciclo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Radio de círculos hemiciclo'),
        ),
        migrations.AlterField(
            model_name='legislatura',
            name='fin',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de cierre'),
        ),
        migrations.CreateModel(
            name='AsientosCongreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_asiento', models.IntegerField(verbose_name='Número asiento')),
                ('posicion_x', models.IntegerField(blank=True, null=True, verbose_name='Posición en el eje X')),
                ('posicion_y', models.IntegerField(blank=True, null=True, verbose_name='Posición en el eje Y')),
                ('congreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asientos', to='congreso.Congreso')),
            ],
            options={
                'unique_together': {('congreso', 'num_asiento')},
            },
        ),
    ]
