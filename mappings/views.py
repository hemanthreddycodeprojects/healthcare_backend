from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class PatientDoctorMappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(PatientDoctorMapping, pk=self.kwargs["pk"])
        return obj
