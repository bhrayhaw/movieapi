from django.contrib import admin
from .models import Movie, StreamPlatform, Reviews

# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(Reviews)
