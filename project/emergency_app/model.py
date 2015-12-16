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
    buildingcode = models.CharField(db_column='buildingCode', primary_key=True, max_length=2, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Building'


class Diagnosis(models.Model):
    diagnosisno = models.IntegerField(db_column='diagnosisNo', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Diagnosis'


class Employee(models.Model):
    empid = models.CharField(db_column='empId', primary_key=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
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
    hospitalid = models.CharField(db_column='hospitalId', primary_key=True, max_length=3, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Hospital'


class Incidentreport(models.Model):
    eventid = models.IntegerField(db_column='eventId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, db_column='empId')  # Field name made lowercase.
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='startDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='endDateTime')  # Field name made lowercase.
    narrative = models.CharField(max_length=1500, blank=True, null=True)
    hospitalid = models.ForeignKey(Hospital, db_column='hospitalId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncidentReport'


class Medication(models.Model):
    medicationno = models.IntegerField(db_column='medicationNo', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    medication = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Medication'


class Recorddiagnosistbl(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN')  # Field name made lowercase.
    diagnosisno = models.ForeignKey(Diagnosis, db_column='diagnosisNo')  # Field name made lowercase.
    daignosisdate = models.DateField(db_column='daignosisDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecordDiagnosistbl'


class Recordmedicationtbl(models.Model):
    rmid = models.IntegerField(primary_key=True)
    mrn = models.ForeignKey('Residentmedicalrecord', db_column='MRN')  # Field name made lowercase.
    medicationno = models.ForeignKey(Medication, db_column='medicationNo')  # Field name made lowercase.
    medstartdate = models.DateField(db_column='medStartDate')  # Field name made lowercase.
    medenddate = models.DateField(db_column='medEndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecordMedicationtbl'


class Residentmedicalrecord(models.Model):
    mrn = models.IntegerField(db_column='MRN', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=20)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=20)  # Field name made lowercase.
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    roomno = models.IntegerField(db_column='roomNo', blank=True, null=True)  # Field name made lowercase.
    buildingcode = models.ForeignKey(Building, db_column='buildingCode', blank=True, null=True)  # Field name made lowercase.
    hospitalpreference = models.CharField(db_column='hospitalPreference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emergencycontacts = models.CharField(db_column='emergencyContacts', max_length=500)  # Field name made lowercase.
    emergencyphoneno = models.CharField(db_column='emergencyPhoneNo', max_length=10)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=10)  # Field name made lowercase.
    phonetype = models.CharField(db_column='phoneType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResidentMedicalRecord'


class Vitalsigns(models.Model):
    uniqueid = models.IntegerField(db_column='uniqueId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    eventid = models.ForeignKey(Incidentreport, db_column='eventId')  # Field name made lowercase.
    empid = models.ForeignKey(Employee, db_column='empId')  # Field name made lowercase.
    assesmdatetime = models.DateTimeField(db_column='assesmDateTime')  # Field name made lowercase.
    vitaltype = models.ForeignKey('Vitalsignstype', db_column='vitalType')  # Field name made lowercase.
    results = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VitalSigns'


class Vitalsignstype(models.Model):
    typecode = models.CharField(db_column='typeCode', primary_key=True, max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'VitalSignsType'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
