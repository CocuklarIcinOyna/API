# Generated by Django 2.1.5 on 2019-01-13 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyExecutive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=15)),
                ('gsm_no', models.CharField(max_length=25)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocuklaricin_api.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('cancel_time', models.DateTimeField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('is_canceled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('map_url', models.URLField()),
                ('fund_raise_date', models.DateField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocuklaricin_api.Campaign')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocuklaricin_api.Fund')),
            ],
        ),
    ]
