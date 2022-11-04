from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, EventGuestSerializer
from .models import Event


class EventsViewList(APIView):
    def get(self, request):
        event_list = Event.objects.all()
        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)


class EventViewSet(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'post': serializer.data})

    def patch(self, request, **kwargs):
        pass

    def get(self, request):
        event = Event.objects.get(pk='event_id')
        serializer = EventSerializer(event)
        return Response({'post': serializer.data})

    def delete(self, request):
        event = Event.objects.get(pk='event_id')
        if event:
            try:
                event.delete()
            except:
                return Response({'post': 'Could not delete this event'})
            return Response({'post': 'Deleted'})
        else:
            return Response({'post': 'Could not find searching event'})



class EventGuestView(APIView):
    def post(self, request):
        serializer = EventGuestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request):
        pass


class EventDenyView(APIView):
    pass