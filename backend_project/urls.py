from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/mgi/', include('mgicandles.urls')),
    path('api/newidea/', include('trading_ideas.urls')),
    path('api/tracker/', include('tradetracker.urls')),
]

# Serve media files during development
if settings.DEBUG:  # Only serve media files when in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
