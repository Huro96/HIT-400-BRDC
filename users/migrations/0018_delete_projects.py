# Generated by Django 4.0.3 on 2022-04-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_rename_description_projects_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
