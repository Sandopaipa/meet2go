from django.urls import path
from .views import EventsViewList

urlpatterns = [
    path('events/list', EventsViewList.as_view())
]