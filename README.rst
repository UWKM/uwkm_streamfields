UWKM WAGTAIL STREAMFIELDS
=========================

This is a set of pre-defined streamfields for Wagtail. It provides:

- accordions
- background image with text overlay
- buttons
- call to action buttons
- colored block
- divider
- image gallery
- bootstrap grid
- header
- icon blocks
- image blocks
- quotation lists
- raw html block
- slider
- slogans
- tabs
- tables
- text fields
- youtube video blocks

This packages comes with a set of html templates, which you might want to tweak
or modify.

Installing uwkm_streamfields
============================

1. Install the package using pip: `pip install uwkm_streamfields`.
2. Add `wagtail.contrib.table_block` to `INSTALLED_APPS` in your project settings.
3. Add `uwkm_streamfields` to `INSTALLED_APPS` in your project settings.
4. Add `SF_TEXT_COLORS` and `SF_BACKGROUND_COLORS` to your project settings.

Default
::
    SF_TEXT_COLORS = [
        ('black', 'Black'),
        ('white', 'White'),
        ('pink', 'Pink'),
    ]

    SF_BACKGROUND_COLORS = [
        ('black', 'Black'),
        ('white', 'White'),
        ('pink', 'Pink'),
    ]


5. Add import `from uwkm_streamfields.models import STREAMFIELDS` to your project models.
6. Use the `STREAMFIELDS` as such:
::
    class SomePage(Page):
        some_content = StreamField(
            STREAMFIELDS,
            null=True,
            blank=True
        )

        content_panels = [
            StreamFieldPanel('some_content'),
        ]

