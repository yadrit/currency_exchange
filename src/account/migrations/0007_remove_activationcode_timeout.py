# Generated by Django 2.2.10 on 2020-03-22 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200322_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationcode',
            name='timeout',
        ),
    ]