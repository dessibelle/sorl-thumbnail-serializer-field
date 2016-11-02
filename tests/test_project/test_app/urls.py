from django.conf.urls import url, include
from rest_framework import routers
from .api import TestModelViewSet


router = routers.DefaultRouter()
router.register(r'test_models', TestModelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
