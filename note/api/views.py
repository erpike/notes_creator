from rest_framework import generics

from note.models import Note
from .serializers import NoteModelSerializer


class NoteCreateAPIView(generics.CreateAPIView):
    serializer_class = NoteModelSerializer


class NoteListAPIView(generics.ListAPIView):
    serializer_class = NoteModelSerializer

    def get_queryset(self, **kwargs):
        qs = Note.objects.all()
        qs = sorted(qs, key=lambda x: x.get_unqiue_words_qty())
        return qs
