# Generated by Django 3.1.2 on 2020-10-28 11:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201028_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 28, 11, 15, 25, 830843, tzinfo=utc)),
        ),
    ]
