from __future__ import unicode_literals
from django.test import TestCase
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

# try:
#     import unittest2 as unittest
# except ImportError:
#     import unittest

# try:
#     from unittest.mock import patch, Mock, ANY, call
# except ImportError:
#     from mock import patch, Mock, ANY, call


class HyperlinkedSorlImageFieldTest(TestCase):

    def test_to_representation(self):
        field = HyperlinkedSorlImageField('1234')

        retval = field.to_representation("value")

        self.assertEqual(None, retval)
        pass
