# Generated by Django 4.0.3 on 2022-04-22 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_tarrifs_comment_alter_ratescomments_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rates',
            new_name='Projects',
        ),
    ]