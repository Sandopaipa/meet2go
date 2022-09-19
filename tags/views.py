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


class TagCreateView(APIView):
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class TagGetView(APIView):
    def get(self, request, tag_id):
        try:
            tag = Tag.objects.get(pk=tag_id)
        except:
            return Response({"post": "Can not find a tag: id is not valid"})
        serializer = TagSerializer(tag, many=False)
        return Response({"post": serializer.data})
