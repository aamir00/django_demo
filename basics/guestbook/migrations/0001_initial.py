# Generated by Django 2.2.2 on 2019-06-08 21:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2019, 6, 8, 21, 13, 27, 96153, tzinfo=utc))),
            ],
        ),
    ]