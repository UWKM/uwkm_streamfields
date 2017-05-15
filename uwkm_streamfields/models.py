from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
        InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from .blocks import *

from .icons import IconChoiceBlock


TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 108,
    'language': 'nl',
    'renderer': 'text',
    'autoColumnSize': False,
}


STREAMFIELDS = [('grid', blocks.ListBlock(
        GridBlock(),
        template = 'streamfields/grid.html',
        icon='grip',))
    ,('tables', TableBlock(
        label='Tabellen',
        table_options=TABLE_OPTIONS,
        template = 'streamfields/table.html',))
    ,('quotes', blocks.ListBlock(
        QuoteBlock(),
        template = 'streamfields/quotes.html',
        icon="openquote",))
    ,('headings', blocks.ListBlock(
        HeaderBlock(),
        template = 'streamfields/header.html',
        icon="title",))
    ,('text_fields', blocks.ListBlock(
        TextFieldBlock(),
        template = 'streamfields/text_field.html',
        icon="doc-full",))
    ,('accordions', blocks.ListBlock(
        AccordionBlock(),
        template = 'streamfields/accordion.html',
        icon='list-ol',))
    ,('tabs', blocks.ListBlock(
        TabBlock(),
        template = 'streamfields/tab.html',
        icon='list-ol',))
    ,('background_with_text', blocks.ListBlock(
        BackgroundBlock(),
        template = 'streamfields/background_with_text.html',
        icon='doc-full',))
    ,('colored_block', blocks.ListBlock(
        ColoredTextBlock(),
        template = 'streamfields/colored_block.html',
        icon="doc-full-inverse",))
    ,('gallery', blocks.ListBlock(
        GalleryBlock(),
        template = 'streamfields/gallery.html',
        icon='image',))
    ,('image', GalleryBlock(
        template = 'streamfields/image.html',
        icon='image'))
    ,('slogans', blocks.ListBlock(
        SloganBlock(),
        template = 'streamfields/slogans.html',
        icon="list-ul",))
    ,('divider', blocks.ListBlock(
        DividerBlock(),
        template = 'streamfields/divider.html',
        icon="horizontalrule",))   
    ,('raw_html', blocks.ListBlock(
        HTMLBlock(),
        template = 'streamfields/raw_html.html',
        icon="code",))
    ,('button', blocks.ListBlock(
        ButtonBlock(),
        template = 'streamfields/button.html',
        icon="tick",))
    ,('video', blocks.ListBlock(
        VideoBlock(),
        template = 'streamfields/video.html',
        icon="media",))
    ,('icon_block', blocks.ListBlock(
        IconBlock(),
        template = 'streamfields/icon_block.html',
        icon="doc-empty",))
    ,('call_to_action', blocks.ListBlock(
        CallToActionBlock(),
        template = 'streamfields/call_to_action.html',
        icon="tick",))
    ,('slider', blocks.ListBlock(
        SliderBlock(),
        template = 'streamfields/slider.html',
        icon="image"))
]
