# Generated by Django 4.1.2 on 2022-11-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='location',
            field=models.CharField(default='NOT SPECIFIED', max_length=150),
        ),
        migrations.AlterField(
            model_name='trackprocess',
            name='identifierProcess',
            field=models.CharField(default='ID::2022-11-12 00:37:33.839809', max_length=1000),
        ),
    ]
