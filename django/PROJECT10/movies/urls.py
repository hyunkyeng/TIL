from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('scores/<int:score_pk>/', views.score_update_and_delete),
    path('movies/<int:movie_pk>/scores/', views.score_create),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/', views.movie_list),
    path('docs/', get_swagger_view(title='Api Docs')),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('genres/', views.genre_list),    
]