from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'homepage/index.html'

class AboutBlogView(TemplateView):
    template_name = 'homepage/about_blog.html'

class AboutCVView(TemplateView):
    template_name = 'homepage/about_cv.html'