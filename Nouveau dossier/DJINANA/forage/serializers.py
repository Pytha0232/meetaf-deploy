from rest_framework import serializers
from . import models

         
        
class LocalisationForageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocalisationForage
        fields = '__all__'
     

    
class EtatEauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EtatEau
        fields = '__all__'