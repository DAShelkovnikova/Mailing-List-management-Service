from django.urls import path
from django.views.decorators.cache import cache_page

from blog1.apps import Blog1Config
from blog1.views import BlogDetailView

app_name = Blog1Config.name

urlpatterns = [
    path("<int:pk>/", cache_page(200)(BlogDetailView.as_view()), name="blog_detail")
]