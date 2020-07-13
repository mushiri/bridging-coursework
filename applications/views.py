from .models import App
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

class AppListView(ListView):
    model = App
    template_name = 'applications/home.html'

class AppDetailView(DetailView):
    model = App
    template_name = 'applications/app_detail.html'

class AppCreateView(CreateView):
    model = App
    template_name = 'applications/app_new.html'
    fields = ['author', 'description', 'image_main', 'image_detail']

class AppUpdateView(UpdateView):
    model = App
    template_name = 'applications/app_edit.html'
    fields = ['description', 'image_main', 'image_detail']

class AppDeleteView(DeleteView):
    model = App
    template_name = 'applications/app_delete.html'
    success_url = reverse_lazy('home_applications')