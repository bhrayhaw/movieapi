from .models import Movie, StreamPlatform, Reviews
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
class MovieSerializer(serializers.ModelSerializer):
    movie_review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist_platforms = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

        
