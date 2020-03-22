# Generated by Django 2.2.10 on 2020-03-22 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_activationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activation_codes', to=settings.AUTH_USER_MODEL),
        ),
    ]
