from django.urls import path
from django.urls.conf import path, include

# drf root

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('etude_des_differenes_problemes',api.ProblemeViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]