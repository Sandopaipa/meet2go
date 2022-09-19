from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tag
from .serializers import TagSerializer
from rest_framework.response import Response

# Create your views here.
class TagListView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response({"post": serializer.data})