# Generated by Django 2.2.5 on 2019-09-21 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sobremi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobremi',
            old_name='imageC',
            new_name='image',
        ),
    ]