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

models.py
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

settings.py
::
    BS_SIZE = 'sm'
    STREAMFIELDS = '__all__'
    EXCLUDE_STREAMFIELDS = []


9. Make sure you atleast have the following javascripts/stylesheets in your base.html

base.html
::
    {# Global stylesheets #}
    <link href="{% static 'css/bootstrap.min.css' %}" type="text/css" rel="stylesheet" />
    <link href="{% static 'fonts/font-awesome-4.7.0/css/font-awesome.min.css' %}" type="text/css" rel="stylesheet" />
    <link href="{% static 'css/streamfields.css' %}" type="text/css" rel="stylesheet" />
    <link href="{% static 'css/owl.carousel.css' %}" type="text/css" rel="stylesheet" />
    <link href="{% static 'css/revolution_slider.css' %}" type="text/css" rel="stylesheet" />

    {# Global javascript #}
    <script type="text/javascript" src="{% static 'js/jquery-2.2.3.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/isotope.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/owl.carousel.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/magnific-popup.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/revolution.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/tools.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/revolution_slider.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/slick.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/custom.js' %}"></script>


10. Extra:

add to templates/wagtailadmin/admin_base.html (if overridden)
::
    {% block css %}
    ...
    <link rel="stylesheet" href="{% static 'css/custom-admin.css' %}" type="text/css" />
    {% endblock %}


    {% block js %}
    ...
    <script type="text/javascript">var collapse = '{{ settings.uwkm_streamfields.streamfieldssettings.collapse_streamfields }}' == 'True';</script>
    <script src="{% static 'js/custom-admin.js' %}"></script>
    <script src="{% static 'js/colorPicker.js' %}"></script>
    ...
    {% endblock %}


UWKM, 2017
