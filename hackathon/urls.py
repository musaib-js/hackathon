from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils import timezone
from datetime import date


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('students/', include('students.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
