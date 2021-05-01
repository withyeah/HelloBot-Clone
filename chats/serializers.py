from rest_framework import serializers

from .models import Scenario, Tarot

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"

class TarotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarot
        fields = "__all__"
