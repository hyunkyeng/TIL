from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, GenreDetailSerializer, MovieSerializer, MovieDetailSerializer, ScoreSerializer
from .models import Genre, Movie, Score

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
    
@api_view(['POST'])
def score_create(request, movie_pk):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)
        return Response({'message':'작성되었습니다.'})

@api_view(['PUT', 'DELETE'])
def score_update_and_delete(request, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.method=='PUT':
        serializer = ScoreSerializer(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    
    else:
        score.delete()
        return Response({'message': '삭제되었습니다'})
    
