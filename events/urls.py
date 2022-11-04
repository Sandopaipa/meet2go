from django.urls import path
from .views import *


#all events list
#All events of user
urlpatterns = [
    path('event/list', EventsViewList.as_view()),
    path('event/<int:event_id>/', EventViewSet.as_view()),

]