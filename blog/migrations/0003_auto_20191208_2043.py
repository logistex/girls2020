# Generated by Django 2.2.7 on 2019-12-08 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191126_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 11, 43, 47, 533575, tzinfo=utc)),
        ),
    ]