from django.urls import include, path

from .views import NoteCreateView, NoteListView

app_name = 'note'

urlpatterns = [
    path(r'', NoteListView.as_view(), name='list'),
    path(r'create/', NoteCreateView.as_view(), name='create'),
]


