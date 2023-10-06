from django.urls import path
from .views import registrationview, logoutview
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registrationview, name='register'),
    path('logout/', logoutview, name='logout'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
]
