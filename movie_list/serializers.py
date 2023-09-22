from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    is_released = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.is_released = validated_data.get(
            'is_released', instance.is_released)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) > 30:
            raise serializers.ValidationError("Name must be at least 30 characters")
        return value
