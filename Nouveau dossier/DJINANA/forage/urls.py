from django.urls import path
from django.urls.conf import path, include

# drf root

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('Localisation de forage',api.LocalisationForageViewSet)
router.register("Etat_d_eau",api.EtatEauViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]