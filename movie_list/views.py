from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from .serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from .models import Movie, StreamPlatform, Reviews
from .permissions import AdminOrReadOnly, ReviewerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reviews.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)

        reviewer = self.request.user
        review_queryset = Reviews.objects.filter(
            movie=movie, reviewer=reviewer)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed")

        if movie.number_of_ratings == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating +
                                serializer.validated_data['rating'])/2

        movie.number_of_ratings += 1
        movie.save()

        serializer.save(movie=movie, reviewer=reviewer)


class ReviewsList(generics.ListAPIView):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']

        return Reviews.objects.filter(movie=pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewerOrReadOnly]
    # authentication_classes = []


class StreamPlatformView(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadOnly]
class MovieListView(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
