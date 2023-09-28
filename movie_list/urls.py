from .views import MovieListView, MovieDetailView, StreamPlatformView, StreamPlatformDetailView, ReviewDetails, ReviewsList
from django.urls import path

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_lists'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_details'),
    path('streamplatforms/', StreamPlatformView.as_view(), name='stream_platform'),
    path('streamplatform/<int:pk>', StreamPlatformDetailView.as_view(),
         name='stream_platform_detail'),
    path('reviews/', ReviewsList.as_view(), name='review'),
    path('reviews/<int:pk>', ReviewDetails.as_view(), name='review-details'),
]
