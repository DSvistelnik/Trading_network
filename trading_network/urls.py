from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/schema', SpectacularAPIView.as_view(), name='swagger'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='swagger')),
    path('user/', include('authentication.urls')),

]
