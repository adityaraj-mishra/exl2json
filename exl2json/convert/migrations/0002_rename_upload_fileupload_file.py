# Generated by Django 4.0.2 on 2022-06-15 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='upload',
            new_name='file',
        ),
    ]
