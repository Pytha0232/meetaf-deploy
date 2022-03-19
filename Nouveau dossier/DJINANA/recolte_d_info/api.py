from . import models
from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers
from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters


class InformationViewSet (viewsets.ModelViewSet):
    queryset = models.Information.objects.filter(status=True)
    serializer_class = serializers.InformationSerializer
    filter_fields = ('nom',)