from .views import movie_lists, movie_details
from django.urls import path

urlpatterns = [
    path('', movie_lists, name='movie_lists'),
    path('<int:pk>/', movie_details, name='movie_details'),  
]
