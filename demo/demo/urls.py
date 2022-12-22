from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from demo import demo_project, settings
from demo.demo_project import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(demo_project.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
