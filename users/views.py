from django.shortcuts import render
from django.contrib.auth import get_user_model, login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

AuthUser = get_user_model()

class SignUpAPIView(APIView):
    def post(self, request):
        try:
            AuthUser.objects.create_user(**request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class SignInView(APIView):
    def post(self, request):
        
        return 
