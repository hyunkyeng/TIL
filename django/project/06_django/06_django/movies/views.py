from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('id')
    return render(request, 'movies/index.html', {'movies': movies})
    
def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movies': movies})
    
def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('/movies/')