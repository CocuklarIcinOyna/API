# Generated by Django 2.1.5 on 2019-01-20 09:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cocuklaricin_api', '0008_auto_20190120_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 9, 47, 1, 128522, tzinfo=utc)),
        ),
    ]
