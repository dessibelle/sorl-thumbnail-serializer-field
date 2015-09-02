from django.conf.urls import url, include
from models import TestModel
from rest_framework import routers, serializers, viewsets
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField


class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel

    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    image = HyperlinkedSorlImageField('1024')


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


router = routers.DefaultRouter()
router.register(r'test_models', TestModelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
