# Generated by Django 3.2 on 2021-05-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(max_length=100)),
                ('from_currency_name', models.CharField(max_length=100)),
                ('to_currency_code', models.CharField(max_length=100)),
                ('to_currency_name', models.CharField(max_length=100)),
                ('exchange_rate', models.CharField(max_length=100)),
                ('last_refreshed', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=100)),
                ('bid_price', models.CharField(max_length=100)),
                ('ask_price', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'quotes',
                'managed': True,
            },
        ),
    ]
