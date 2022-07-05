from rest_framework import serializers
from . import models

         
        
class LocalisationForageSerializer(serializers.ModelSerializer):

    partenaire = models.LocalisationForage.objects.count()
    forage = models.LocalisationForage.objects.all()

    class Meta:
        model = models.LocalisationForage
        fields = '__all__'


    
class EtatEauSerializer(serializers.ModelSerializer):
    def  
    class Meta:
        model = models.EtatEau
        fields = '__all__'