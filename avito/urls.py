from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from ads.views.ad import AdViewSet
from avito import settings
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('ad', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', include('ads.urls.category')),
    path('selection/', include('ads.urls.selection')),
    path('user/', include('users.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'))
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
