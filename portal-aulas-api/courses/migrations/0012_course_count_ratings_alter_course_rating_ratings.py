# Generated by Django 4.0.10 on 2023-05-22 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0011_course_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='count_ratings',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
