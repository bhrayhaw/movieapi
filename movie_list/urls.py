from .views import MovieListView, MovieDetailView
from django.urls import path

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_lists'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_details'),  
]
