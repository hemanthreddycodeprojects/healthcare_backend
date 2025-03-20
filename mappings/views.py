from django.shortcuts import render
from rest_framework import generics
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from rest_framework.permissions import IsAuthenticated

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

class PatientDoctorMappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
