from rest_framework import serializers
from .models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('state_text', 'state_code', 'country')

    def create(self, validated_data):
        return State.objects.create(**validated_data)

    def update(self, instance, data):
        instance.state_text = data.get('state_text', instance.state_text)
        instance.state_code = data.get('state_code', instance.state_code)
        instance.country = data.get('country_code', instance.country)
        instance.save()
        return instance
