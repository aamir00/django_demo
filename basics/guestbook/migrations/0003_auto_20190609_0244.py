# Generated by Django 2.2.2 on 2019-06-08 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20190609_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 21, 14, 19, 52254, tzinfo=utc)),
        ),
    ]
