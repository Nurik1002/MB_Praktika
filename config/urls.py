from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('images/', include('image_filters.urls')),
    path("ailabs/", include('ailab.urls')),
    path('posts/', include('post.urls')),
    path('ajax/', include('ajax.urls')),
    path('consultation/', include("consultation.urls")),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)