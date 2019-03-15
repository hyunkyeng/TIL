from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Genre, Movie, Score

# Create your views here.
def index(request):
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()

    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
    
def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    comments = movie.score_set.all()
    context = {
        'movie': movie, 
        'genre': genre, 
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:index')

def score_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    comment = Score()
    comment.movie = movie
    comment.content = request.POST.get('content')
    comment.score = request.POST.get('score')
    
    comment.save()
    return redirect('movies:detail', movie.pk)
    
def score_delete(request, movie_pk, score_pk):
    comment = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('movies:detail', movie_pk)
    else:
        return redirect('movies:detail', movie_pk)
    
    