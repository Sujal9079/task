# Generated by Django 2.2 on 2024-03-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp', '0002_subject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
