from __future__ import unicode_literals
from django.test import TestCase
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework.test import APIRequestFactory
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from sorl.thumbnail import get_thumbnail
from .api import TestModelViewSet
from .models import TestModel
import mock


def mock_to_native(obj, value):
    return "ORIGINAL_URL"


class HyperlinkedSorlImageFieldTest(TestCase):

    def setUp(self):
        self.image1 = self.create_image("RGBA", (2048, 1536), (255, 0, 0, 255), filename="image1.png")
        self.image2 = self.create_image("RGBA", (800, 800), (0, 255, 0, 255), filename="image2.png")

        self.model1 = TestModel.objects.create(name="Image 1", image=self.image1)
        self.model2 = TestModel.objects.create(name="Image 2", image=self.image2)

        self.factory = APIRequestFactory()
        self.model_detail = TestModelViewSet.as_view({'get': 'retrieve'})

    def create_image(self, *args, **kwargs):
        filename = kwargs.pop("filename", "image.png")

        image_file = BytesIO()
        image = Image.new(*args, **kwargs)
        image.save(image_file, 'png')
        image_file.seek(0)

        return ContentFile(image_file.read(), filename)

    def test_to_representation(self):
        field = HyperlinkedSorlImageField("200")
        request = self.factory.get('/api/test_model')
        field.context = {"request": request}

        image = get_thumbnail(self.image1, "200")
        expected_url = request.build_absolute_uri(image.url)
        actual_url = field.to_representation(self.image1)

        self.assertEqual(expected_url, actual_url)

    @mock.patch("rest_framework.serializers.ImageField.to_representation")
    def test_to_representation_no_request(self, mocked_to_representation):
        mocked_to_representation.return_value = "ORIGINAL URL"
        field = HyperlinkedSorlImageField("200")

        image = field.to_representation("URL IMAGE")

        self.assertEqual("ORIGINAL URL", image)

    @mock.patch("rest_framework.serializers.ImageField.to_representation", side_effect=AttributeError())
    @mock.patch("rest_framework.serializers.ImageField.to_native", create=True, new=mock_to_native)
    def test_to_representation_attribute_error(self, mocked_to_representation):
        field = HyperlinkedSorlImageField("200")

        image = field.to_representation("URL IMAGE")
        self.assertEqual("ORIGINAL_URL", image)
