sorl-thumbnail-serializer-field
===============================

A sorl-thumbnail field for use with django-rest-framework

Quick start
-----------

1. Add `sorl_thumbnail_serializer` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'sorl_thumbnail_serializer',
    )

2. Add the `SorlHyperlinkedThumbnailField` to your serializer class.

3. Specify the image dimensions when querying the REST API. Full size URL while be returned if dimensions are not specified.
