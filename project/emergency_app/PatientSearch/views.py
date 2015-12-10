from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from PatientSearch.models import *
from PatientSearch.serializers import ResidentInfoSerializer

# Create your views here.

class ResidentInfoViewSet(viewsets.ReadOnlyModelViewSet):
	model = Resident
	queryset = Resident.objects.all()
	serializer_class = ResidentInfoSerializer
	permission_classes = (IsAuthenticated,)
	
