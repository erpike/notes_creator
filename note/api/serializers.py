from rest_framework import serializers

from note.models import Note

class NoteModelSerializer(serializers.ModelSerializer):
    #qq = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = [
            'content',
            #'qq',
        ]

    # def get_qq(self, obj):
    #     return obj.get_unqiue_words_qty()
