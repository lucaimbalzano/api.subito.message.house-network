# Generated by Django 4.2.1 on 2023-10-05 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_house_dateadded_alter_house_datetimeadded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='dateTimeAdded',
            field=models.TimeField(default=datetime.time(21, 35, 49, 801995)),
        ),
        migrations.AlterField(
            model_name='machineprocess',
            name='startedDateTime',
            field=models.TimeField(default=datetime.time(21, 35, 49, 826653)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='dateTimeSent',
            field=models.TimeField(default=datetime.time(21, 35, 49, 824511)),
        ),
        migrations.AlterField(
            model_name='timemanager',
            name='addedDateTime',
            field=models.TimeField(default=datetime.time(21, 35, 49, 825790)),
        ),
    ]