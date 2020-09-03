# Generated by Django 3.0.8 on 2020-09-03 06:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200903_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.IntegerField(choices=[(2, 'bolivia'), (3, 'peru')])),
                ('monitoreo', models.IntegerField(choices=[(4, 'calidad'), (5, 'biomasa')])),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Ubicación',
                'verbose_name_plural': 'Ubicación',
            },
        ),
        migrations.DeleteModel(
            name='Inicio',
        ),
    ]