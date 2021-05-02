from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Scenario, Tarot


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"


class TarotSerializer(serializers.ModelSerializer):
    card_image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Tarot
        fields = "__all__"
