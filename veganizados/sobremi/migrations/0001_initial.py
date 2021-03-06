# Generated by Django 2.2.5 on 2019-09-21 16:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SobreMi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name="Titulo. Ej: 'Sobre Mí'")),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('imageC', models.ImageField(blank=True, null=True, upload_to='img_sobremi', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Momento de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Momento de edicion')),
            ],
            options={
                'verbose_name': 'Sobre mi',
            },
        ),
    ]
