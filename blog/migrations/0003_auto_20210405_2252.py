# Generated by Django 3.1.7 on 2021-04-05 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210405_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]