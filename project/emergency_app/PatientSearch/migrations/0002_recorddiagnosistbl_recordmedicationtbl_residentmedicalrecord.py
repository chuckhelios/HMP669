# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recorddiagnosistbl',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'RecordDiagnosistbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recordmedicationtbl',
            fields=[
                ('rmid', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'RecordMedicationtbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Residentmedicalrecord',
            fields=[
                ('mrn', models.IntegerField(serialize=False, primary_key=True, db_column='MRN', blank=True)),
                ('namefirst', models.CharField(max_length=20, db_column='nameFirst')),
                ('namelast', models.CharField(max_length=20, db_column='nameLast')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('roomno', models.IntegerField(null=True, db_column='roomNo', blank=True)),
                ('hospitalpreference', models.CharField(max_length=100, db_column='hospitalPreference', blank=True)),
                ('emergencycontacts', models.CharField(max_length=500, db_column='emergencyContacts')),
                ('emergencyphoneno', models.CharField(max_length=10, db_column='emergencyPhoneNo')),
                ('phoneno', models.CharField(max_length=10, db_column='phoneNo')),
                ('phonetype', models.CharField(max_length=20, null=True, db_column='phoneType', blank=True)),
                ('daignosisdesription', models.CharField(max_length=100, db_column='daignosisDesription')),
                ('reasonformedication', models.CharField(max_length=100, db_column='reasonForMedication')),
            ],
            options={
                'db_table': 'ResidentMedicalRecord',
                'managed': False,
            },
        ),
    ]
