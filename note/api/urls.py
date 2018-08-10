from django.urls import path
from .views import NoteCreateAPIView, NoteListAPIView

app_name = 'api_note'

urlpatterns = [
    path(r'', NoteListAPIView.as_view(), name='list'),
    path(r'create/', NoteCreateAPIView.as_view(), name='create'),
]


