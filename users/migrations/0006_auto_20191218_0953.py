# Generated by Django 2.2.5 on 2019-12-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191218_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='terms_and_conditions',
            field=models.BooleanField(default=False),
        ),
    ]
