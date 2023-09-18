from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('admin/', include('admin_dashboard.urls')),
    path('', include('Melhikapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)