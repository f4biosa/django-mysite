from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('snippets.urls')),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("__debug__/", include("debug_toolbar.urls")),
]