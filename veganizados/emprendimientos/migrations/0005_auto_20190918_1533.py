# Generated by Django 2.2.5 on 2019-09-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprendimientos', '0004_auto_20190918_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprendimiento',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre de Emprendimiento'),
        ),
    ]