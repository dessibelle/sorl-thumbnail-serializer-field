from .models import TestModel
from rest_framework import serializers, viewsets
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
