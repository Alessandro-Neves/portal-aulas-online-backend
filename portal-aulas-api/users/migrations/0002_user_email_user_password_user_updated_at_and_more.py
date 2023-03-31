# Generated by Django 4.0.10 on 2023-03-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='default', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]