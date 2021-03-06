# Generated by Django 3.0.8 on 2020-09-03 05:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_lugar_parametros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.IntegerField(choices=[(2, 'bolivia'), (3, 'peru')])),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Inicio',
            },
        ),
        migrations.DeleteModel(
            name='Lugar',
        ),
    ]
