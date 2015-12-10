# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildingcode', models.CharField(max_length=2, serialize=False, primary_key=True, db_column='buildingCode', blank=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Building',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosisno', models.IntegerField(serialize=False, primary_key=True, db_column='diagnosisNo', blank=True)),
                ('daignosisdate', models.DateField(db_column='daignosisDate')),
                ('diagnosis', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='empId', blank=True)),
                ('namefirst', models.CharField(max_length=20, db_column='nameFirst')),
                ('namelast', models.CharField(max_length=20, db_column='nameLast')),
                ('username', models.CharField(max_length=20, db_column='userName')),
                ('password', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=10, db_column='phoneNumber')),
                ('emptype', models.CharField(max_length=3, null=True, db_column='empType', blank=True)),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.CharField(max_length=3, serialize=False, primary_key=True, db_column='hospitalId', blank=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Incidentreport',
            fields=[
                ('eventid', models.IntegerField(serialize=False, primary_key=True, db_column='eventId', blank=True)),
                ('startdatetime', models.DateField(db_column='startDateTime')),
                ('enddatetime', models.DateField(db_column='endDateTime')),
                ('narrative', models.CharField(max_length=1500, null=True, blank=True)),
            ],
            options={
                'db_table': 'IncidentReport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicalrecord',
            fields=[
                ('mrn', models.IntegerField(serialize=False, primary_key=True, db_column='MRN', blank=True)),
                ('daignosisdesription', models.CharField(max_length=100, db_column='daignosisDesription')),
                ('medicationno', models.IntegerField(null=True, db_column='medicationNo', blank=True)),
                ('reasonformedication', models.CharField(max_length=100, db_column='reasonForMedication')),
            ],
            options={
                'db_table': 'MedicalRecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('medicationno', models.IntegerField(serialize=False, primary_key=True, db_column='medicationNo', blank=True)),
                ('medstartdate', models.DateField(db_column='medStartDate')),
                ('medenddate', models.DateField(db_column='medEndDate')),
                ('medication', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Medication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('residentid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='residentId', blank=True)),
                ('namefirst', models.CharField(max_length=20, db_column='nameFirst')),
                ('namelast', models.CharField(max_length=20, db_column='nameLast')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('roomno', models.IntegerField(null=True, db_column='roomNo', blank=True)),
                ('hospitalpreference', models.CharField(max_length=100, null=True, db_column='hospitalPreference', blank=True)),
                ('emergencycontacts', models.CharField(max_length=500, db_column='emergencyContacts')),
                ('emergencyphoneno', models.CharField(max_length=10, db_column='emergencyPhoneNo')),
                ('phoneno', models.CharField(max_length=10, db_column='phoneNo')),
                ('phonetype', models.CharField(max_length=20, null=True, db_column='phoneType', blank=True)),
            ],
            options={
                'db_table': 'Resident',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vitalsigns',
            fields=[
                ('uniqueid', models.IntegerField(serialize=False, primary_key=True, db_column='uniqueId', blank=True)),
                ('assesmdatetime', models.DateField(db_column='assesmDateTime')),
                ('results', models.CharField(max_length=100, null=True, blank=True)),
                ('comments', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
                'db_table': 'VitalSigns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vitalsignstype',
            fields=[
                ('typecode', models.CharField(max_length=1, serialize=False, primary_key=True, db_column='typeCode', blank=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'VitalSignsType',
                'managed': False,
            },
        ),
    ]
