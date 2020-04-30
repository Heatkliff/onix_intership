# Generated by Django 3.0.5 on 2020-04-29 20:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0004_auto_20200429_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={},
        ),
        migrations.AlterField(
            model_name='country',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
