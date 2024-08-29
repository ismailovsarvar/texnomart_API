from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from root import custom_token
from root import settings

urlpatterns = ([
                   path('grappelli/', include('grappelli.urls')),
                   path('admin/', admin.site.urls),
                   path('texnomart-uz/', include('texnomart.urls')),
                   path('api-auth/', include('rest_framework.urls')),
                   path('token-auth/', custom_token.CustomAuthToken.as_view(), name='api_token_auth'),
                   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns += debug_toolbar_urls()
