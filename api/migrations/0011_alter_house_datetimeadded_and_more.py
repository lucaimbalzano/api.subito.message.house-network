# Generated by Django 4.2.1 on 2023-10-05 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_house_datetimeadded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='dateTimeAdded',
            field=models.TimeField(default=datetime.time(21, 54, 40, 299480)),
        ),
        migrations.AlterField(
            model_name='machineprocess',
            name='startedDateTime',
            field=models.TimeField(default=datetime.time(21, 54, 40, 317601)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='dateTimeSent',
            field=models.TimeField(default=datetime.time(21, 54, 40, 316359)),
        ),
        migrations.AlterField(
            model_name='timemanager',
            name='addedDateTime',
            field=models.TimeField(default=datetime.time(21, 54, 40, 317126)),
        ),
    ]
