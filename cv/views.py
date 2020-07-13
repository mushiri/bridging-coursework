from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cv/home.html'

class CardDetailView(DetailView):
    model = Card
    template_name = 'cv/card_detail.html'

class CardCreateView(CreateView):
    model = Card
    template_name = 'cv/card_new.html'
    fields = ['title', 'author', 'body']

class CardUpdateView(UpdateView):
    model = Card
    template_name = 'cv/card_edit.html'
    fields = ['title', 'body']

class CardDeleteView(DeleteView):
    model = Card
    template_name = 'cv/card_delete.html'
    success_url = reverse_lazy('home_cv')