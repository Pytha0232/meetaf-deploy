"""DJINANA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static

# rest api

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Djinana API",
        default_version='v1',
        description="Bienvenu sur la doc",
        terms_of_service="#",
        url='#',
        contact=openapi.Contact(email="knd@gmail.com"),
        license=openapi.License(name="Djinana"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    #sawger
    
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
        
    
]


urlpatterns += [
    path('admin/', admin.site.urls),
    path('website', include('website.urls')),
    path('etude/', include('etude.urls')),
    path('forage/', include('forage.urls')),
    path('recolte_d_info/', include('recolte_d_info.urls')),
]

if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)