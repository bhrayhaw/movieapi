from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from user_app import models


# Create your views here.
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logoutview(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registrationview(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)
