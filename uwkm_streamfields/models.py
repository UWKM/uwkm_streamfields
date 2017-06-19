# UWKM Streamfields.
from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class StreamfieldsSettings(BaseSetting):
    collapse_streamfields = models.BooleanField(
        default=True
    )
    pre_selected_colors = models.TextField(
        verbose_name="Pre-kleuren",
        help_text="Gescheiden kleuren met een ';' (max. 7)",
        blank=True
    )
    google_api_key = models.CharField(
    	max_length=255,
    	help_text="API Key van Google"
    )