# Generated by Django 2.1.1 on 2018-09-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
