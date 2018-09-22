# Generated by Django 2.1.1 on 2018-09-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_auto_20180922_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('foto', models.ImageField(upload_to='fotos-de-actores')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actores',
            field=models.ManyToManyField(blank=True, to='peliculas.Actor'),
        ),
    ]
