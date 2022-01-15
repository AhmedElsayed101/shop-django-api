"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import re
import imp
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.schemas import get_schema_view as openapi_get_schema_view
from dj_rest_auth.registration.views import VerifyEmailView


schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version='v1',
        description="Shop app for Bit68",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

openapi_schema = openapi_get_schema_view(
    title="Products API",
    description="Shop app for Bit68",
    version="1.0.0"
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('products.urls')),
    path("api/v1/auth/", include("rest_framework.urls")),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),

    path('api/v1/rest-auth/registration/account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    re_path('api/v1/rest-auth/registration/',
            include('dj_rest_auth.registration.urls')),


    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),

    path('schema/', openapi_schema)
]
