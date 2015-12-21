
"""
PatientSearch serializers are used to make flat database to JSON format.

**Patient View**
	1. **FilteredResidentSerializer**
	2. **ResidentInfoSerializer**

----
"""
from rest_framework import serializers
from django.forms import widgets
from PatientSearch.models import *

# ================= Patient view ========================== #
class FilteredResidentSerializer(serializers.ListSerializer):
	'''
	:desc: filter search
	'''	
	def to_representation(self, data):
		request = self.context.get('request', None)
		rid = request.query_params.get('id', None)
		f_name = request.query_params.get('fname', None)
		l_name = request.query_params.get('lname', None)
		gender = request.query_params.get('gender', None)
		roomNo = request.query_params.get('room', None)
		buildingNo = request.query_params.get('building', None)

		residents = data

		if rid != None:	
			residents = residents.filter(residentid=rid)
		if f_name != None:
			residents = residents.filter(namefirst__iexact=f_name)
		print len(residents)

		if l_name != None:
			residents = residents.filter(namelast__iexcat=l_name)
		if gender != None:
			residents = residents.filter(gender=gender)
		if roomNo != None:
			residents = residents.filter(roomno=roomNo)
		if buildingNo != None:
			residents = residents.filter(buildingcode=buildingNo)

		return super(FilteredResidentSerializer, self).to_representation(residents)


class FilteredLatestByIdSerializer(serializers.ListSerializer):
	def to_representation(self, data):
		request = self.context.get('request', None)
		last = request.query_params.get('last', None)
		if last != None:
			newdata = [data.order_by('-pk')[0],]
		else:
			newdata = data
		return super(FilteredLatestByIdSerializer, self).to_representation(newdata)

class MedicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medication

class DiagnosisSerializer(serializers.ModelSerializer):
	class Meta:
		model =Diagnosis


class RecordmedicationtblSerializer(serializers.ModelSerializer):
	medicationno = MedicationSerializer('medicationno', many=False)
	class Meta:
		model = Recordmedicationtbl

class RecorddiagnosistblSerializer(serializers.ModelSerializer):
	diagnosisno = DiagnosisSerializer('diagnosisno', many=False)
	class Meta:
		model = Recorddiagnosistbl

class VitalsignstypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vitalsignstype


class VitalsignsPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vitalsigns
 		list_serializer_class = FilteredLatestByIdSerializer

class VitalsignsSerializer(serializers.ModelSerializer):
	vitaltype = VitalsignstypeSerializer('vitaltype', many=False)
	class Meta:
		model = Vitalsigns

class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hospital


class IncidentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Incidentreport
		fields = ('eventid', 'empid', 'mrn', 'startdatetime', 'enddatetime', 'narrative', 'hospitalid' )
 		list_serializer_class = FilteredLatestByIdSerializer


class IncidentreportSerializer(serializers.ModelSerializer):
	# vitalSigns = serializers.SerializerMethodField()
	vitalSigns = VitalsignsSerializer(source='vs_event', many=True)
	hospitalid = HospitalSerializer('hospitalid', many=False)

	class Meta:
		model = Incidentreport
		fields = ('eventid', 'empid', 'startdatetime', 'enddatetime', 'narrative', 'hospitalid', 'vitalSigns' )

class ResidentInfoSerializer(serializers.ModelSerializer):
	'''

	'''
	med = RecordmedicationtblSerializer(source='rm_mrn', many=True)
	diag = RecorddiagnosistblSerializer(source='rd_mrn', many=True)
	incidents = IncidentreportSerializer(source='in_mrn', many=True)

	class Meta:
		model = Residentmedicalrecord
		list_serializer_class = FilteredResidentSerializer
		fields = ('mrn', 'namefirst', 'namelast', 'dob', 'gender', 'roomno', 'buildingcode', 'hospitalpreference', 'emergencycontacts', 'emergencyphoneno', 'phoneno', 'phonetype', 'med', 'diag', 'incidents' )


class BuildingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Building
		


