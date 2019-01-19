# Generated by Django 2.1.5 on 2019-01-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocuklaricin_api', '0004_auto_20190117_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='campaign',
            name='description',
            field=models.TextField(default='', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machine',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
