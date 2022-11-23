# Generated by Django 4.1.2 on 2022-11-23 15:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=500)),
                ('space', models.CharField(max_length=20)),
                ('rooms', models.CharField(max_length=20)),
                ('floor', models.CharField(max_length=20)),
                ('bathrooms', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=100)),
                ('parking', models.CharField(max_length=200)),
                ('energyClass', models.CharField(max_length=50)),
                ('energyHeating', models.CharField(max_length=50)),
                ('urlUserProfile', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('number', models.CharField(max_length=20)),
                ('vetrina', models.BooleanField(default=False)),
                ('advertising', models.CharField(max_length=100)),
                ('location', models.CharField(default='NOT SPECIFIED', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TrackProcess',
            fields=[
                ('identifierProcess', models.AutoField(primary_key=True, serialize=False)),
                ('numPage', models.IntegerField(default=20)),
                ('numCard', models.IntegerField(default=33)),
                ('errorStack', models.CharField(default='NO ERROR', max_length=10000)),
                ('dateStarted', models.DateTimeField(default=datetime.datetime.now)),
                ('dateFinished', models.DateTimeField(blank=True, default=None, null=True)),
                ('options', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('seconds_execution', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('minutes_execution', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateMachineProcess',
            fields=[
                ('id_state_machine', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=10, unique=True)),
                ('processId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.trackprocess')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageName', models.CharField(max_length=100)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=5000)),
                ('numberSent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house')),
            ],
        ),
    ]
