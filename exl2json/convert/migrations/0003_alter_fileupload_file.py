# Generated by Django 4.0.2 on 2022-06-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0002_rename_upload_fileupload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='static/'),
        ),
    ]
