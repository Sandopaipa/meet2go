from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Profile


class FollowViewSet(APIView):
    def patch(self, request, **kwargs):
        pass

