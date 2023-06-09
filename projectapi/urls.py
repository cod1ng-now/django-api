"""
URL configuration for projectapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include("rest_framework.urls")),
    path('api/v1/dj-rest-auth/', include("dj_rest_auth.urls")),
    path('api/v1/dj-rest-auth/registration/', include("dj_rest_auth.registration.urls")),
    path("sxema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/sxema/redoc/", SpectacularSwaggerView.as_view(url_name="schema"), name="redoc"),
]

handler404 = 'app.views.error404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)