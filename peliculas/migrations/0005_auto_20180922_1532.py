# Generated by Django 2.1.1 on 2018-09-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0004_auto_20180922_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos-de-actores'),
        ),
    ]
