from django.core import serializers
from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import ScenarioSerializer, TarotSerializer 
from .models import Scenario, Tarot

# Create your views here.

class ScenarioViewSet(viewsets.ModelViewSet): 
    queryset = Scenario.objects.all() 
    serializer_class = ScenarioSerializer

class TarotViewSet(viewsets.ModelViewSet): 
    queryset = Tarot.objects.all() 
    serializer_class = TarotSerializer

