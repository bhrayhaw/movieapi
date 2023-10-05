from .views import MovieListView, MovieDetailView, StreamPlatformView, ReviewDetails, ReviewsList, ReviewCreate
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('streamplatforms', StreamPlatformView, basename='streamplatforms')

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_lists'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_details'),
    path('', include(router.urls)),
    # path('streamplatform/<int:pk>/', StreamPlatformDetailView.as_view(),
    #      name='stream_platform_detail'),
    # path('reviews/', ReviewsList.as_view(), name='review'),
    # path('reviews/<int:pk>', ReviewDetails.as_view(), name='review-details'),
    path('<int:pk>/reviews-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewsList.as_view(), name='review-list'),
    path('<int:pid>/reviews/<int:pk>/', ReviewDetails.as_view(), name='review-details'),
]
