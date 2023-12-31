# Generated by Django 4.0.10 on 2023-05-27 21:14

import django.core.validators
from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_user_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='password'),
        ),
    ]
