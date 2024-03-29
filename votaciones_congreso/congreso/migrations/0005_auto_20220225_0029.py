# Generated by Django 3.0.3 on 2022-02-25 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0004_auto_20220225_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='hemiciclo',
            name='congreso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hemiciclos', to='congreso.Congreso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hemiciclo',
            name='fin',
            field=models.DateField(null=True, verbose_name='Fecha de fin'),
        ),
    ]
