# Generated by Django 4.1.7 on 2023-02-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('citizen_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('intelligence', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'citizen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('criminal_id', models.AutoField(primary_key=True, serialize=False)),
                ('weapons', models.TextField()),
                ('hostages', models.SmallIntegerField()),
                ('number_of_crimes', models.SmallIntegerField()),
                ('threat_coefficient', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'criminal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PsychoPassport',
            fields=[
                ('series', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('crime_rate', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'psycho_passport',
                'managed': False,
            },
        ),
    ]