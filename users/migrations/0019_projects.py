# Generated by Django 4.0.3 on 2022-04-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_delete_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_number', models.CharField(max_length=10, verbose_name='Rates')),
                ('name', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField()),
            ],
        ),
    ]
