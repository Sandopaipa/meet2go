from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event


class EventsViewList(APIView):
    def get(self, request):
        event_list = Event.objects.all()
        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)
