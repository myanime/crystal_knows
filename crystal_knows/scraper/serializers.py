from rest_framework import serializers
from scraper.models import Scraper

class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraper
        fields = ('pk','first_name','last_name','about_person')
        
    def create(self, validated_data):
        """
        Used when calling Serializer.save()
        """
        return Scraper.objects.create(**validated_data)
