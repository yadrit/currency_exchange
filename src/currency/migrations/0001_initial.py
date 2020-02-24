# Generated by Django 2.2.10 on 2020-02-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'USD'), (2, 'EUR')])),
                ('buy', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.PositiveSmallIntegerField(choices=[(1, 'PrivatBank'), (2, 'Monobank')])),
            ],
        ),
    ]