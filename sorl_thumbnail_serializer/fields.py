from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class HyperlinkedSorlImageField(serializers.ImageField):

    def __init__(self, dimensions, options={}, *args, **kwargs):

        self.dimensions = dimensions
        self.options = options

        super(HyperlinkedSorlImageField, self).__init__(*args, **kwargs)

    def to_native(self, value):

        image = get_thumbnail(value, self.dimensions, **self.options)

        try:
            request = self.context.get('request', None)
            return request.build_absolute_uri(image.url)
        except Exception, e:
            return super(HyperlinkedSorlImageField, self).to_native(image.url)
