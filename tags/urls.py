from .views import TagGetView, TagCreateView, TagListView
from django.urls import path

urlpatterns = [
    path('tag/list', TagListView.as_view()),
    path('tag/<int:tag_id>', TagGetView.as_view()),
    path('tag/create', TagCreateView.as_view()),
]
