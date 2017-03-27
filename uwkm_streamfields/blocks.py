from django.conf import settings

from django import forms 
from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

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



class ColorChoiceBlock(blocks.ChoiceBlock):
    try:
        choices = setting.SF_BACKGROUND_COLORS
    except:
        choices = [
            ('black', 'Black'),
            ('white', 'White'),
        ]

class TextColorChoiceBlock(blocks.ChoiceBlock):
    try:
        choices = setting.SF_TEXT_COLORS
    except:
        choices = [
            ('black', 'Black'),
            ('white', 'White'),
        ]

class AlignChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    ]

class GridChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('col-xs-12', '12'),
        ('col-xs-11', '11'),
        ('col-xs-10', '10'),
        ('col-xs-9', '9'),
        ('col-xs-8', '8'),
        ('col-xs-7', '7'),
        ('col-xs-6', '6'),
        ('col-xs-5', '5'),
        ('col-xs-4', '4'),
        ('col-xs-3', '3'),
        ('col-xs-2', '2'),
        ('col-xs-1', '1'),
    ]


class SliderBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    name = blocks.CharBlock(
        label='Name',
        max_length = 30,
        help_text = 'Name of caption.',
        required = True,
    )

    subtext = blocks.CharBlock(
        label='Subtext',
        max_length = 35,
        help_text = 'Caption.',
        required = False,
    )

    button = blocks.BooleanBlock(
        label='Call to Action',
        default=False,
        help_text = 'Has call to action button.',
        required = False,
    )

    cta_text = blocks.CharBlock(
        label='CTA text',
        max_length = 20,
        required = False,
    )

    cta_pos  = blocks.ChoiceBlock(
		label = 'CTA position',
        choices = (
            ('left', _('Left')),
            ('right', _('Right'))
        ),
        required = False,
    )

    cta_color = ColorChoiceBlock(
        label = 'CTA background URL',
        required = False,
    )

    cta_link_type = blocks.ChoiceBlock(
        label = 'CTA link type',
        choices = (
            ('wagtail', 'Wagtailpage'),
            ('url', 'Manual url')
        ),
        required = False,
    )

    cta_page_link = blocks.PageChooserBlock(
        label = 'CTA wagtail link',
        can_choose_root = True,
        required= False,
    )

    cta_url = blocks.CharBlock(
        label='CTA url',
        max_length = 255,
        required = False,
    )

    class Meta:
        icon = 'image'

class SloganBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    title = blocks.CharBlock(
        label = 'Caption',
        max_length = 30,
        help_text = 'Caption of the slide.',
        required = True,
    )

    text = blocks.TextBlock(
        label = 'Text',
        max_length = 120,
    )

class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(
        label = 'Quote',
        required = True,
        max_length = 150,
    )

    logo = ImageChooserBlock(required = False)

    name = blocks.CharBlock(
        label = 'Name',
        max_length = 50,
        help_text = 'Name of the person.',
    )

    company = blocks.CharBlock(
        label = 'Company',
        max_length = 50,
        help_text = 'Company.',
    )

    city = blocks.CharBlock(
        label = 'City',
        max_length = 50,
        help_text = 'City.'
    )


class HeaderChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('h1', 'Heading one'),
        ('h2', 'Heading two'),
        ('h3', 'Heading three'),
        ('h4', 'Heading four'),
        ('h5', 'Heading five'),
        ('h6', 'Heading six'),
    )


class HeaderBlock(blocks.StructBlock):
    header = HeaderChoiceBlock(
        label = 'Heading',
        help_text = 'Size of the heading.'
    )
    text = blocks.CharBlock(
        label = 'Text',
        max_length = 50,
        help_text = 'Text of the heading.',
    )


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label = 'Title',
        max_length = 50,
        help_text = 'Tabtitle.',
    )
    content = blocks.RichTextBlock(
        label = 'Content',
        help_text = 'Tabcontent.',
    )


class TabBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label = 'Title',
        max_length = 50,
        help_text = 'Tabtitle.',
    )
    content = blocks.RichTextBlock(
        label = 'Content',
        help_text = 'Tabcontent.',
    )


class TextFieldBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(
        label = 'Textfield',
        help_text = 'Content of the text field',
    )


class BackgroundBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(
        label = 'Image',
        help_text = 'A background image',
    )
    block_height = blocks.IntegerBlock(
        label = 'Height',
        help_text = 'Height of the parallax image (in pixels).',
        min_value = 0,
        max_value = 999,
        default = 250,
    )
    text = blocks.RichTextBlock(
        label = 'Text',
        help_text = 'Text in the background.',
        required = False,
    )
    text_color = TextColorChoiceBlock(
        label = 'Text color',
        required = False,
    )
    align = AlignChoiceBlock(
        label = 'Align',
    )


class ColoredTextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Text',
        required = False,
    )
    text_color = TextColorChoiceBlock(
        label = 'Color text',
        required = False,
    )
    background_color = ColorChoiceBlock(
        label = 'Backgroundcolor',
        required = False,
    )


class GalleryBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        label = 'Image',
        help_text = 'An image in a gallery.',
    )


class DividerBlock(blocks.StructBlock):
    border_color = blocks.ChoiceBlock(
        choices = [('primary', 'Primaire'),],
        label = 'Divider',
        help_text = 'Divider color.',
    )


class HTMLBlock(blocks.StructBlock):
    raw_html = blocks.RawHTMLBlock(
        label = 'HTML',
        help_text = 'Raw HTML',
    )


class ButtonBlock(blocks.StructBlock):
    button_class = ColorChoiceBlock(
        label = 'Layout class',
        help_text = 'Layout class of the button',
    )
    icon = IconChoiceBlock(
        label = 'Icon',
        help_text = 'Icon oin the button. (Font awesome)',
        required = False,
    )
    text = blocks.CharBlock(
        label = 'Text',
        max_length = 50,
        help_text = 'Text in the button',
    )
    width = blocks.ChoiceBlock(
        label = 'Width',
        choices = [
            (' ', 'Auto'), ('btn-block', '100%'),
        ]
    )
    link = blocks.PageChooserBlock(
        label = 'Link',
        can_choose_root = True,
        required= False,
    )
    ext_link = blocks.CharBlock(
        label='External link',
        max_length = 255,
        required = False,
    )

class VideoBlock(blocks.StructBlock):
    video_id = blocks.CharBlock(
        label = 'Video',
        max_length = 11,
        help_text = 'YouTube video code/id.',
    )

class IconBlock(blocks.StructBlock):
    icon = IconChoiceBlock(
        label = 'Icon',
        help_text = 'Icon. (Font awesome)',
    )
    text = blocks.RichTextBlock(
        label = 'Text',
        help_text = 'Text in the block',
    )

class CallToActionBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Text',
        help_text = 'Text in the block',
    )
    button = ButtonBlock()


class GridBlock(blocks.StructBlock):
    grid = GridChoiceBlock(
        label = 'Column width',
        help_text = 'Bootstrap column width.',
    )
    content = blocks.StreamBlock(
        [('tables', TableBlock(
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
        ],
    )
