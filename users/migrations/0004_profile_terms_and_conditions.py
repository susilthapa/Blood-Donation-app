# Generated by Django 2.2.5 on 2019-12-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191216_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='terms_and_conditions',
            field=models.BooleanField(default=False),
        ),
    ]