# Generated by Django 4.2.5 on 2024-03-05 14:44

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]
