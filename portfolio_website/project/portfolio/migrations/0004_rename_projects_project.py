# Generated by Django 4.2.6 on 2023-10-24 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_projects_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]