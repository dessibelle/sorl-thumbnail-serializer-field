from django.conf import settings

SORL_THUMBNAIL_SETTINGS = getattr(settings, "SORL_THUMBNAIL_SETTINGS", {})

SORL_THUMBNAIL_SETTINGS.setdefault("URI_PREFIX", None)
