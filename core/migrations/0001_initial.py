# Generated by Django 3.0.7 on 2020-06-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('carnet', models.IntegerField(primary_key=True, serialize=False)),
                ('paterno', models.CharField(max_length=150)),
            ],
        ),
    ]