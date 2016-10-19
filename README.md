Sorl  Thumbnail Serializer Field
===============================

[![Build Status](https://travis-ci.org/dessibelle/sorl-thumbnail-serializer-field.svg?branch=master)](https://travis-ci.org/dessibelle/sorl-thumbnail-serializer-field) [![Coverage Status](https://coveralls.io/repos/github/dessibelle/sorl-thumbnail-serializer-field/badge.svg?branch=master)](https://coveralls.io/github/dessibelle/sorl-thumbnail-serializer-field?branch=master)

An image serializer field for use with sorl and Django REST Framework.

Provides an easy way of exposing a scaled version of an image rather than the
full-size one, and if you prefer several different versions (thumb, large etc.)

Quick start
-----------

1. Add the `HyperlinkedSorlImageField` to your serializer class.

2. Specify the image dimensions and cropping options that the REST API should use.


Example usage
-------------
```python
# urls.py
from django.conf.urls import url, include
from models import TestModel
from rest_framework import routers, serializers, viewsets
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField


class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel

    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    # A larger version of the image, allows writing
    image = HyperlinkedSorlImageField('1024')


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


router = routers.DefaultRouter()
router.register(r'test_models', TestModelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
```
