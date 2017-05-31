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
4. Add `from uwkm_streamfields.settings.base import *` to your project settings.
5. Add import `from uwkm_streamfields.blocks import GridBlock` to your project models.
6. Use the `GridBlock` as such:

::
    class SomePage(Page):
        some_content = StreamField(
            [('fixed_width', blocks.ListBlock(
                GridBlock(),
                template = 'streamfields/fixed_grid.html',
                icon='fa-th-large',
                label='Boxed'))
            ,('full_width', blocks.ListBlock(
                GridBlock(),
                template = 'streamfields/full_grid.html',
                icon='fa-th',
                label='Full'))
            ],
            null = True,
            blank = True
        )

        content_panels = Page.content_panels + [
            StreamFieldPanel('some_content'),
        ]

7. Use `some_content` as such:

somepage.html
::
    {% for block in page.some_content %}
        {{ block }}
    {% endfor %}

8. Change the settings as you like:

::
    BS_SIZE = 'sm'

    CP_COLORS = [
        '#0099ff',
        '#00cc00',
        '#ffff00',
        '#ff6600',
        '#cc0000',
        '#ffffff',
        '#000000',
    ]

    STREAMFIELDS = '__all__'
    EXCLUDE_STREAMFIELDS = []



UWKM, 2017
