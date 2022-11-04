from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .models import Tag
from .serializers import TagSerializer
from rest_framework.response import Response


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

class TagUpdateView(APIView):
#Staff only
    permission_classes = [IsAdminUser, ]
    def patch(self, request, tag_id, **kwargs):
        tag_id = kwargs.get('tag_id', None)
        if tag_id:
            try:
                tag = Tag.objects.get(pk=tag_id)
            except:
                return Response({'post': 'tag is not defined'})
            tag_serializer = TagSerializer(data=request.data, instance=tag, partial=True)
            tag_serializer.is_valid(raise_exception=True)
            tag_serializer.save()
            return Response({'post': tag_serializer.data})

    def delete(self, request, tag_id, **kwargs):
        tag_id = kwargs.get('tag_id', None)
        if tag_id:
            try:
                tag = Tag.objects.get(pk=tag_id)
            except:
                return Response({'post': 'tag is not defined'})
            tag.delete()
            return Response({'post': 'tag has been deleted'})