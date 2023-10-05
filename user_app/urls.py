from django.urls import path
from .views import registrationview, logoutview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registrationview, name='register'),
    path('logout/', logoutview, name='logout'),
]
