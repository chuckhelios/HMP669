
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
		buildingNo = request.query_params.get('buiding', None)

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


class MedicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medication

class DiagnosisSerializer(serializers.ModelSerializer):
	class Meta:
		model = Diagnosis


class MedicalrecordSerializer(serializers.ModelSerializer):
	''''''
	diagosis = DiagnosisSerializer(source='residentid') 
	class Meta:
		model = Medicalrecord


class ResidentInfoSerializer(serializers.ModelSerializer):
	'''

	'''
	class Meta:
		model = Resident
		list_serializer_class = FilteredResidentSerializer



class IncidentreportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Incidentreport


