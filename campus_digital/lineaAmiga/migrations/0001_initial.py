# Generated by Django 4.2.1 on 2023-05-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineaAmiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='linea amiga', verbose_name='Imagen')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenidos',
            },
        ),
    ]