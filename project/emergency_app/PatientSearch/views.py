from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_bulk import BulkModelViewSet

from PatientSearch.models import *
from PatientSearch.serializers import *

# Create your views here.

class ResidentInfoViewSet(viewsets.ReadOnlyModelViewSet):
	model = Residentmedicalrecord
	queryset = Residentmedicalrecord.objects.all()
	serializer_class = ResidentInfoSerializer
	permission_classes = (IsAuthenticated,)
	

class IncidentViewSet(viewsets.ModelViewSet):
	model = Incidentreport
	queryset = Incidentreport.objects.all()
	serializer_class = IncidentSerializer
	permission_classes = (IsAuthenticated,)

class IncidentReportViewSet(viewsets.ModelViewSet):
	model = Incidentreport
	queryset = Incidentreport.objects.all()
	serializer_class = IncidentreportSerializer
	permission_classes = (IsAuthenticated,)


class VitalsignsViewSet(BulkModelViewSet):
	model = Vitalsigns
	queryset = Vitalsigns.objects.all()
	serializer_class = VitalsignsPostSerializer
	permission_classes = (IsAuthenticated,)

class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
	model = Building
	queryset = Building.objects.all()
	serializer_class = BuildingSerializer
	permission_classes = (IsAuthenticated,)