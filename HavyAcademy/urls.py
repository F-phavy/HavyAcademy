"""
URL configuration for HavyAcademy project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# 1. IMPORT your Signup view from your core app
from core.views import SignUpView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('core.urls', namespace='core')),
    path('students/', include('student_management.urls', namespace='students'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)