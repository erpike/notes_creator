from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView

from .forms import NoteCreateForm
from .models import Note

# Create your views here.
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm

    def get_success_url(self):
        return reverse('note:list')


class NoteListView(ListView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NoteCreateForm()
        return context