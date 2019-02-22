from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/', views.detail, name="detail"),
    path('', views.index, name="index"),
]