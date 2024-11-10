from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('messages1.urls', namespace='message')),
    path("users/", include("users1.urls", namespace="users")),
    path("blog/", include("blog1.urls", namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
