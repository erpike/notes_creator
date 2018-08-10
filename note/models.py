from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

    def get_unqiue_words_qty(self):
        return len(set(self.content.split(' ')))