# Generated by Django 4.1.3 on 2023-10-24 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='image',
        ),
    ]
