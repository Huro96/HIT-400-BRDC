# Generated by Django 4.0.1 on 2022-03-08 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_tarrifs_alter_blockcontacts_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarrifs',
            old_name='updat_date',
            new_name='update_date',
        ),
        migrations.AlterField(
            model_name='ratescomments',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 8, 12, 28, 59, 238825, tzinfo=utc)),
        ),
    ]
