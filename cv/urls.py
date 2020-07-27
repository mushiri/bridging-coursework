from django.urls import path
from .views import (
    CardListView,
    CardDetailView,
    CardCreateView,
    CardUpdateView,
    CardDeleteView,
)

urlpatterns = [
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
    path('card/<int:pk>/edit/', CardUpdateView.as_view(), name='card_edit'),
    path('card/new/', CardCreateView.as_view(), name='card_new'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('', CardListView.as_view(), name='card_list'),
]