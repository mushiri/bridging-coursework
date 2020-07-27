from django.urls import path, include
from .views import (
    HomePageView,
    AboutBlogView,
    AboutCVView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about-blog/', AboutBlogView.as_view(), name='about_blog'),
    path('about-cv/', AboutCVView.as_view(), name='about_cv'),
    path('blog/', include('blog.urls')),
    path('cv/', include('cv.urls')),
]

