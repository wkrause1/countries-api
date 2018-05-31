from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_text' , 'country_code')

    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.country_text = validated_data.get('country_text', instance.country_text)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.save()
        return instance
