from rest_framework import serializers

from note.models import Note


class NoteModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'content',
        ]

