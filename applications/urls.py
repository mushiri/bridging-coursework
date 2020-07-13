from django.urls import path
from .views import (
    AppListView,
    AppDetailView,
    AppCreateView,
    AppUpdateView,
    AppDeleteView,
)

urlpatterns = [
    path('app/<int:pk>/delete/', AppDeleteView.as_view(), name='app_delete'),
    path('app/<int:pk>/edit/', AppUpdateView.as_view(), name='app_edit'),
    path('app/new/', AppCreateView.as_view(), name='app_new'),
    path('app/<int:pk>/', AppDetailView.as_view(), name='app_detail'),
    path('', AppListView.as_view(), name='home_applications'),
]