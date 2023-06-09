"""
URL configuration for blog project.

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

import debug_toolbar
from django.conf import settings

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework import routers
# from cms import views

# router = routers.DefaultRouter()

# router.register(r'posts', views.PostViewSet)
# router.register(r'authors', views.AuthorViewSet)
# router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    # path('', include(router.urls)),
    path('', include('cms.urls')),
    path('blog/', include('cms.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

    # path('', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]