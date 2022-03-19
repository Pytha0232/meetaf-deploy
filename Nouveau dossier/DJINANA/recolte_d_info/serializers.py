from rest_framework import serializers
from . import models

         
        
class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Information
        fields = '__all__'
