from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AccountData
from .serializers import UserSerializer, CreateUserSerializer

class UserListView(APIView):
    def get(self, request):
        accounts = AccountData.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)

class CreateUserView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)
