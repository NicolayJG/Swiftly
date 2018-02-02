# Generated by Django 2.0.1 on 2018-02-01 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20180201_1530'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='restaurante',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurante'),
        ),
        migrations.AlterField(
            model_name='platillo',
            name='tamaño',
            field=models.CharField(blank=True, choices=[('P', 'Pequeño'), ('G', 'Grande'), ('M', 'Medio')], default='M', max_length=1),
        ),
    ]