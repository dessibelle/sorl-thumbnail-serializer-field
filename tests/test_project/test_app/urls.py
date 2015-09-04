from django.conf.urls import url, include
from api import TestModelViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test_models', TestModelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
