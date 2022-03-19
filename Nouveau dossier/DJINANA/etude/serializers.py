from rest_framework import serializers
from . import models

         
        
class ProblemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Probleme
        fields = '__all__'
     