# Generated by Django 5.1.4 on 2024-12-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=10)),
                ('currency_name', models.CharField(max_length=100)),
                ('exchange_rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
