# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Building(models.Model):
    buildingcode = models.CharField(db_column='buildingCode', primary_key=True, max_length=2, blank=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Building'


class Diagnosis(models.Model):
    diagnosisno = models.IntegerField(db_column='diagnosisNo', primary_key=True, blank=True,)  # Field name made lowercase.
    diagnosis = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Diagnosis'


class Employee(models.Model):
    empid = models.CharField(db_column='empId', primary_key=True, max_length=10, blank=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=20)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=20)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10)  # Field name made lowercase.
    emptype = models.CharField(db_column='empType', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class Hospital(models.Model):
    hospitalid = models.CharField(db_column='hospitalId', primary_key=True, max_length=3, blank=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Hospital'


class Incidentreport(models.Model):
    eventid = models.IntegerField(db_column='eventId', primary_key=True, blank=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, db_column='empId', related_name='in_empid')  # Field name made lowercase.
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN', related_name='in_mrn')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='startDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='endDateTime')  # Field name made lowercase.
    narrative = models.CharField(max_length=1500, blank=True, null=True)
    hospitalid = models.ForeignKey(Hospital, db_column='hospitalId', related_name='in_hos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncidentReport'


class Medication(models.Model):
    medicationno = models.IntegerField(db_column='medicationNo', primary_key=True, blank=True)  # Field name made lowercase.
    medication = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Medication'


class Recorddiagnosistbl(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN', related_name='rd_mrn')  # Field name made lowercase.
    diagnosisno = models.ForeignKey(Diagnosis, db_column='diagnosisNo', related_name='rd_diag')  # Field name made lowercase.
    daignosisdate = models.DateField(db_column='daignosisDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecordDiagnosistbl'


class Recordmedicationtbl(models.Model):
    rmid = models.IntegerField(primary_key=True)
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN', related_name='rm_mrn')  # Field name made lowercase.
    medicationno = models.ForeignKey(Medication, db_column='medicationNo', related_name='rm_med')  # Field name made lowercase.
    medstartdate = models.DateField(db_column='medStartDate')  # Field name made lowercase.
    medenddate = models.DateField(db_column='medEndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecordMedicationtbl'


class Residentmedicalrecord(models.Model):
    mrn = models.IntegerField(db_column='MRN', primary_key=True, blank=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=20)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=20)  # Field name made lowercase.
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    roomno = models.IntegerField(db_column='roomNo', blank=True, null=True)  # Field name made lowercase.
    buildingcode = models.ForeignKey(Building, db_column='buildingCode', blank=True, related_name='rmr_building')  # Field name made lowercase.
    hospitalpreference = models.CharField(db_column='hospitalPreference', max_length=100, blank=True)  # Field name made lowercase.
    emergencycontacts = models.CharField(db_column='emergencyContacts', max_length=500)  # Field name made lowercase.
    emergencyphoneno = models.CharField(db_column='emergencyPhoneNo', max_length=10)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=10)  # Field name made lowercase.
    phonetype = models.CharField(db_column='phoneType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # medications = models.ManyToManyField(Medication, through='Recordmedicationtbl')
    # diagnosis = models.ManyToManyField(Diagnosis, through='Recorddiagnosistbl')

    class Meta:
        managed = False
        db_table = 'ResidentMedicalRecord'


class Vitalsigns(models.Model):
    uniqueid = models.IntegerField(db_column='uniqueId', primary_key=True, blank=True)  # Field name made lowercase.
    eventid = models.ForeignKey(Incidentreport, db_column='eventId', related_name='vs_event')  # Field name made lowercase.
    empid = models.ForeignKey(Employee, db_column='empId', related_name='vs_empid')  # Field name made lowercase.
    assesmdatetime = models.DateTimeField(db_column='assesmDateTime')  # Field name made lowercase.
    vitaltype = models.ForeignKey('Vitalsignstype', db_column='vitalType', related_name='vs_vt')  # Field name made lowercase.
    results = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VitalSigns'


class Vitalsignstype(models.Model):
    typecode = models.CharField(db_column='typeCode', primary_key=True, max_length=1, blank=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'VitalSignsType'


