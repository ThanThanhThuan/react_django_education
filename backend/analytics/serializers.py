from rest_framework import serializers
from .models import EducationData

class EducationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationData
        fields = '__all__'