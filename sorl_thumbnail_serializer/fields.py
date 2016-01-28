"""
An image serializer field for use with sorl and Django REST Framework.

Provides an easy way of exposing a scaled version of an image rather than the
full-size one, and if you prefer many different versions (thumb, large etc.)

Example Usage:

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
"""

from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class HyperlinkedSorlImageField(serializers.ImageField):

    """A Django REST Framework Field class returning hyperlinked scaled and cached images."""

    def __init__(self, geometry_string, options={}, *args, **kwargs):
        """
        Create an instance of the HyperlinkedSorlImageField image serializer.

        Args:
            geometry_string (str): The size of your cropped image.
            options (Optional[dict]): A dict of sorl options.
            *args: (Optional) Default serializers.ImageField arguments.
            **kwargs: (Optional) Default serializers.ImageField keyword
            arguments.

        For a description of sorl geometry strings and additional sorl options,
        please see https://sorl-thumbnail.readthedocs.org/en/latest/examples.html?highlight=geometry#low-level-api-examples
        """  # NOQA
        self.geometry_string = geometry_string
        self.options = options

        super(HyperlinkedSorlImageField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        """
        Perform the actual serialization.

        Args:
            value: the image to transform
        Returns:
            a url pointing at a scaled and cached image
        """
        if not value:
            return None

        image = get_thumbnail(value, self.geometry_string, **self.options)

        try:
            request = self.context.get('request', None)
            return request.build_absolute_uri(image.url)
        except:
            try:
                return super(HyperlinkedSorlImageField, self).to_representation(image.url)
            except AttributeError:  # NOQA
                return super(HyperlinkedSorlImageField, self).to_native(image.url)  # NOQA
    to_native = to_representation
