from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title', 'audience', 'poster_url', 'description', 'genre',]
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'movies',]
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre',]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['content', 'score',]
