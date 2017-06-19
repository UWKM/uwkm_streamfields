from django.conf import settings

from django import forms 
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from .icons import IconChoiceBlock
from .widgets import ColorPickerWidget

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



class ColorPickerBlock(blocks.FieldBlock):
    def __init__(self, required=True, **kwargs):
        self.field = forms.CharField(required=required, widget=ColorPickerWidget)
        super(ColorPickerBlock, self).__init__(**kwargs)


class AlignChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    ]

class GridChoiceBlock(blocks.ChoiceBlock):
    BS_SIZE = settings.BS_SIZE
    choices = [
        ('col-%s-12' % BS_SIZE, '12'),
        ('col-%s-11' % BS_SIZE, '11'),
        ('col-%s-10' % BS_SIZE, '10'),
        ('col-%s-9' % BS_SIZE, '9'),
        ('col-%s-8' % BS_SIZE, '8'),
        ('col-%s-7' % BS_SIZE, '7'),
        ('col-%s-6' % BS_SIZE, '6'),
        ('col-%s-5' % BS_SIZE, '5'),
        ('col-%s-4' % BS_SIZE, '4'),
        ('col-%s-3' % BS_SIZE, '3'),
        ('col-%s-2' % BS_SIZE, '2'),
        ('col-%s-1' % BS_SIZE, '1'),
    ]


class MasonryGalleryBlock(blocks.StructBlock):
    columns = blocks.ChoiceBlock(
        label = 'Kolommen',
        default = '4',
        choices = (
            ('2', '2 kolommen'),
            ('3', '3 kolommen'),
            ('4', '4 kolommen'),
            ('5', '5 kolommen'),
            ('6', '6 kolommen'),
        )
    )
    big_img = blocks.IntegerBlock(
        label = 'Grote afbeelding',
        required = False,
        help_text = 'Optioneel: hoeveelste plaatje (uit onderstaande afbeeldingen) wordt een "groot plaatje".'
    )
    image = blocks.ListBlock(
        ImageChooserBlock(),
        icon='image',
        label='Afbeelding',
    )


class SliderBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    name = blocks.CharBlock(
        label='Naam',
        max_length = 30,
        help_text = 'Verschijnt onderaan als navigatieknop.',
        required = True,
    )

    subtext = blocks.CharBlock(
        label='Subtekst',
        max_length = 35,
        help_text = 'Verschijnt onder de navigatieknop.',
        required = False,
    )

    button = blocks.BooleanBlock(
        label='Call to Action',
        default=False,
        help_text = 'Heeft een call to action knop.',
        required = False,
    )

    cta_text = blocks.CharBlock(
        label='CTA tekst',
        max_length = 20,
        required = False,
    )

    cta_pos  = blocks.ChoiceBlock(
        label = 'CTA Positie',
        choices = (
            ('left', _('Left')),
            ('right', _('Right'))
        ),
        required = False,
    )
    
    cta_color_picker = ColorPickerBlock(
        label = 'CTA achtergrondkleur kiezer',
        required = False,
    )

    cta_link_type = blocks.ChoiceBlock(
        label = 'CTA link type',
        choices = (
            ('wagtail', 'Wagtailpagina'),
            ('url', 'Handmatige url')
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
        label = 'Naam',
        max_length = 30,
        help_text = 'Verschijnt onderaan als navigatieknop.',
        required = True,
    )

    text = blocks.TextBlock(
        label = 'Tekst',
        max_length = 120,
    )

class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(
        label = 'Citaat',
        required = True,
        max_length = 150,
    )

    quote_pos = blocks.ChoiceBlock(
        choices = (
            ('up', 'Boven'),
            ('under', 'Onder'),
        ),
        label = 'Positie quote',
        help_text = 'De positie van de quote (boven of onder het plaatje).',
    )

    quote_size = blocks.ChoiceBlock(
        choices = (
            ('24px', '24px'),
            ('40px', '40px'),
        ),
        label = 'Quote tekstgrootte',
        help_text = 'De tekstgroote van de quote.',
    )

    quote_background_color = ColorPickerBlock(
        label = 'Achtergrondkleur',
        required = False,
        help_text = 'De achtergrondkleur van de quote.'
    )
    quote_color = ColorPickerBlock(
        label = 'Kleur tekst',
        required = False,
        help_text = 'De tekstkleur van de quote.'
    )

    logo = ImageChooserBlock(required = False)

    name = blocks.CharBlock(
        label = 'Naam',
        max_length = 50,
        help_text = 'Naam van de persoon achter het citaat.',
    )

    company = blocks.CharBlock(
        label = 'Bedrijf',
        max_length = 50,
        help_text = 'Naam van het bedrijf achter het citaat.',
    )

    city = blocks.CharBlock(
        label = 'Plaats',
        max_length = 50,
        help_text = 'Plaats'
    )

    link = blocks.PageChooserBlock(
        label = 'Interne link',
        can_choose_root = True,
        required = False,
    )



class HeaderChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    )


class HeaderBlock(blocks.StructBlock):
    header = HeaderChoiceBlock(
        label = 'Kopgrootte',
        help_text = 'Grootte van de tekst.'
    )
    text = blocks.CharBlock(
        label = 'Tekst',
        max_length = 50,
        help_text = 'Tekst van de koptekst.',
    )


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label = 'Titel',
        max_length = 50,
        help_text = 'Tekst in de titel.',
    )
    content = blocks.RichTextBlock(
        label = 'Inhoud',
        help_text = 'Inhoud van de tab.',
    )


class TabBlock(blocks.StructBlock):
    icon = IconChoiceBlock(
        label = 'Icoon',
        help_text = 'Icoon. (Font awesome)',
        required = False,
    )
    title = blocks.CharBlock(
        label = 'Titel',
        max_length = 50,
        help_text = 'Tekst in de titel.',
    )
    content = blocks.RichTextBlock(
        label = 'Inhoud',
        help_text = 'Inhoud van de tab.',
    )

class UnorderedListBlock(blocks.StructBlock):
    bullet_icon = ImageChooserBlock(
        label = 'Afbeelding-icoon',
        help_text = 'Het afbeelding icoontje per bullet.',
        required=False,
    )
    content = blocks.ListBlock(
        blocks.RichTextBlock(),
        label = 'Bullets',
        help_text = 'Inhoud van de bullet.',
    )

class TextFieldBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(
        label = 'Tekstveld',
        help_text = 'Inhoud van het tekstveld.',
    )

class InfoBoxBlock(blocks.StructBlock):
    tekst = blocks.RichTextBlock()

    class Meta:
        template = 'streamfields/infoblock.html'

class BackgroundBlock(blocks.StructBlock):
    type_field = blocks.ChoiceBlock(
        choices=(
            ('parallaxBg', 'Parallax'),
            ('fixedBg', 'Stilstaand'),
        )
    )
    background_image = ImageChooserBlock(
        label = 'Afbeelding',
        help_text = 'Het achtergrondplaatje van het blok.',
    )
    block_height = blocks.IntegerBlock(
        label = 'Hoogte',
        help_text = 'Hoogte van het blok in pixels.',
        min_value = 0,
        max_value = 999,
        default = 250,
    )
    columns = blocks.ChoiceBlock(
        label = 'Kolommen',
        choices = [('2', 'Twee'), ('1', 'Een')],
        default = '2',
    )
    text_left = blocks.RichTextBlock(
        label = 'Tekst links',
        help_text = 'Tekst aan de linkerkant op de achtergrond.',
        required = False,
    )
    text_right = blocks.RichTextBlock(
        label = 'Tekst rechts',
        help_text = 'Tekst aan de rechterkant op de achtergrond.',
        required = False,
    )
    text_color = ColorPickerBlock(
        label = 'Kleur tekst',
        required = False,
    )


class ColoredTextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Tekst',
        required = False,
    )
    color = ColorPickerBlock(
        label = 'Kleur kiezer',
        required = False,
    )
    bg_color = ColorPickerBlock(
        label = 'Achtergrondkleur kiezer',
        required = False,
    )



class DividerBlock(blocks.StructBlock):
    border_color = ColorPickerBlock(
        label = 'Divider',
        help_text = 'Lijn kleur.',
    )
    border_width = blocks.IntegerBlock(
        default=2, 
        min_value=1, 
        max_value=50, 
        help_text="De dikte van de horizontal lijn.", 
        label="Dikte"
    ) 


class HTMLBlock(blocks.StructBlock):
    raw_html = blocks.RawHTMLBlock(
        label = 'HTML blok',
        help_text = 'HTML blok',
    )


class ButtonBlock(blocks.StructBlock):
    button_color = ColorPickerBlock(
        label = 'Achtergrondkleur kiezer',
        help_text = 'De kleur van de achtergrond.',
        required = False,
    )
    color = ColorPickerBlock(
        label = 'Fontkleur kiezer',
        help_text = 'De kleur van de tekst.',
        required = False,
    )
    icon = IconChoiceBlock(
        label = 'Icoon',
        help_text = 'Icoon op de knop. (Font awesome)',
        required = False,
    )
    icon_size = blocks.IntegerBlock(
        label = 'Icoon grootte',
        help_text = 'Grootte van de icoon op de knop. (in pixels)',
        default = 14,
    )
    text = blocks.CharBlock(
        label = 'Tekst',
        max_length = 50,
        help_text = 'Tekst op de knop.',
    )
    text_size = blocks.IntegerBlock(
        label = 'Tekst grootte',
        help_text = 'Grootte van de tekst op de knop. (in pixels)',
        default = 14,
    )
    width = blocks.ChoiceBlock(
        label = 'Breedte',
        choices = [
            (' ', 'Automatisch'), ('btn-block', '100%'),
        ]
    )
    link = blocks.PageChooserBlock(
        label = 'Link',
        can_choose_root = True,
        required= False,
        help_text="Kies een van de twee: link / externe link."
    )
    ext_link = blocks.CharBlock(
        label='Externe link',
        max_length = 255,
        required = False,
        help_text="Kies een van de twee: link / externe link."
    )

class VideoBlock(blocks.StructBlock):
    video_id = blocks.CharBlock(
        label = 'Video',
        max_length = 11,
        help_text = 'YouTube video code/id.',
    )

class IconBlock(blocks.StructBlock):
    align = AlignChoiceBlock(
        label = 'Uitlijning',
        help_text = 'Uitlijning van de tekst.'
    )
    icon = IconChoiceBlock(
        label = 'Icoon',
        help_text = 'Icoon. (Font awesome)',
    )
    text = blocks.RichTextBlock(
        label = 'Tekst',
        help_text = 'Tekst in het blok.',
    )

class CallToActionBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Tekst',
        help_text = 'Tekst in het blok.',
    )
    button = ButtonBlock()




class TableStructBlock(blocks.StructBlock):
    type_table = blocks.ChoiceBlock(
        choices = [(' ', 'Gewone tabel'), ('price-table', 'Prijs tabel')],
        label='Type tabel',
    )
    table_borders = blocks.ChoiceBlock(
        choices = [
            ('no-borders', 'Geen lijnen'), ('column-borders', 'Kolom lijnen'),
            ('row-borders', 'Regel lijnen'), ('all-borders', 'Kolom en regel lijnen'),
        ],
        label='Tabel lijnen'
    )
    table_header_rows = blocks.IntegerBlock(
        label = 'Tabelheaderrijen',
        min_value = 0,
        max_value = 100,
        default = 2,
    )
    table_footer_rows = blocks.IntegerBlock(
        label = 'Tabelfooterrijen',
        min_value = 0,
        max_value = 100,
        default = 2,
    )
    table_header_background = ColorPickerBlock(
        label = 'Tabelheader achtergrondkleur',
        required = False,
    )
    table_header_color = ColorPickerBlock(
        label = 'Tabelheader tekstkleur',
        required = False,
    )
    table_header_text_size = blocks.IntegerBlock(
        label = 'Tabelheader grootte tekst',
        help_text = 'Tabelheader grootte van de tekst.',
        min_value = 1,
        max_value = 100,
        default = 20,
    )
    table_footer_background = ColorPickerBlock(
        label = 'Tabelfooter achtergrondkleur',
        required = False,
    )
    table_footer_color = ColorPickerBlock(
        label = 'Tabelfooter tekstkleur',
        required = False,
    )
    table = TableBlock(
        table_options=TABLE_OPTIONS,
        label='Tabel',
        help_text='HTML is mogelijk in de tabel'
    )


class ActionBlock(blocks.StructBlock):
    action = blocks.CharBlock(verbose_name="Actie", help_text="Tekst wat linksboven in de afbeelding komt. Bijvoorbeeld: Blog")
    color = ColorPickerBlock(
        label = 'Achtergrond kleur',
        help_text='Achtergrond kleur voor actie',
        required = False,
    )
    image = ImageChooserBlock()
    datum = blocks.DateBlock(required=False, help_text="Optioneel. Bijvoorbeeld voor blogs of speciale events.")
    title = blocks.CharBlock(verbose_name="Titel", help_text="Titel van je actieblok. Voorbeeld: Review: De nieuwe HP Latex 570")
    link = blocks.CharBlock(verbose_name="Link url", help_text="Vul hier een url handmatig in. Bijvoorbeeld: /contact/ of www.google.nl")
    link_text = blocks.CharBlock(verbose_name="Link tekst", help_text="Vul hier een url tekst handmatig in. Bijvoorbeeld: bekijk alle blogartikelen of bekijk alle reviews. ")


class LogoBlock(blocks.StructBlock):
    link = blocks.PageChooserBlock()
    icon = ImageChooserBlock()
    title = blocks.CharBlock(blank=True,default='')
    image = ImageChooserBlock()


class DownloadLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True,default='')
    buttontext = blocks.CharBlock(blank=True,default='')
    link = DocumentChooserBlock()
    image = ImageChooserBlock()

class RevSliderBlock(blocks.StructBlock):
    image = ImageChooserBlock()


class OwlGalleryBlock(blocks.StructBlock):
    image = ImageChooserBlock()


class CoworkerBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255,blank=True)
    roepnaam = blocks.CharBlock(max_length=255, null=True,blank=True)
    job_function = blocks.CharBlock(max_length=255, blank=True, null=True)
    address = blocks.CharBlock(max_length=255, blank=True, null=True, required=False,)
    email = blocks.EmailBlock(max_length=254, blank=True, null=True, required=False,)
    phone = blocks.CharBlock(max_length=255, blank=True, null=True, required=False,)
    linkedin = blocks.URLBlock(max_length=200, blank=True, null=True, required=False,)
    positions = blocks.IntegerBlock(default=1)
    image = ImageChooserBlock()

class ProjectBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True,default='')
    image = ImageChooserBlock()
    link = blocks.PageChooserBlock()

    
class GoogleMapsBlock(blocks.StructBlock):
    address = blocks.TextBlock(
        label = 'Adres',
        help_text = 'Adres, plaats, land',
        required = False,
    )
    height = blocks.IntegerBlock(
        label = 'Hoogte',
        help_text = 'Hoogte van het blok in pixels.',
        min_value = 0,
        max_value = 999,
        default = 250,
    )



grid_array = \
    [('tabellen', TableStructBlock(
        label='Tabellen',
        template = 'streamfields/table.html',
        icon='fa-table'))
    ,('citaten', blocks.ListBlock(
        QuoteBlock(),
        template = 'streamfields/quotes.html',
        icon="openquote",))
    ,('koppen', blocks.ListBlock(
        HeaderBlock(),
        template = 'streamfields/header.html',
        icon="title",))
    ,('tekst_velden', blocks.ListBlock(
        TextFieldBlock(),
        template = 'streamfields/text_field.html',
        icon="fa-align-justify",))
    ,('lijst', blocks.ListBlock(
        UnorderedListBlock(),
        template = 'streamfields/list.html',
        icon="list-ul"))
    ,('accordions', blocks.ListBlock(
        AccordionBlock(),
        template = 'streamfields/accordion.html',
        icon='list-ol',))
    ,('tabs', blocks.ListBlock(
        TabBlock(),
        template = 'streamfields/tab.html',
        icon='list-ol',))
    ,('verticale_tabs', blocks.ListBlock(
        TabBlock(),
        template = 'streamfields/vertical_tab.html',
        icon='list-ol',))    
    ,('afbeelding_met_tekst', blocks.ListBlock(
        BackgroundBlock(),
        template = 'streamfields/background_with_text.html',
        icon='doc-full',))
    ,('gekleurde_blokken', blocks.ListBlock(
        ColoredTextBlock(),
        template = 'streamfields/colored_block.html',
        icon="doc-full-inverse",))
    ,('masonry_gallerij', blocks.ListBlock(
        MasonryGalleryBlock(),
        template = 'streamfields/masonry_gallery.html',
        icon='fa-th',))
    ,('owl_gallerij', blocks.ListBlock(
        OwlGalleryBlock(),
        template = 'streamfields/owl_gallery.html',
        icon='image',))
    ,('afbeelding', blocks.ListBlock(
        ImageChooserBlock(),
        template = 'streamfields/image.html',
        icon='image'))
    ,('divider', blocks.ListBlock(
        DividerBlock(),
        template = 'streamfields/divider.html',
        icon="horizontalrule",))   
    ,('html', blocks.ListBlock(
        HTMLBlock(),
        template = 'streamfields/raw_html.html',
        icon="code",))
    ,('knop', blocks.ListBlock(
        ButtonBlock(),
        template = 'streamfields/button.html',
        icon="fa-hand-pointer-o",))
    ,('video', blocks.ListBlock(
        VideoBlock(),
        template = 'streamfields/video.html',
        icon="media",))
    ,('icoon', blocks.ListBlock(
        IconBlock(),
        template = 'streamfields/icon_block.html',
        icon="fa-font-awesome",))
    ,('call_to_action', blocks.ListBlock(
        CallToActionBlock(),
        template = 'streamfields/call_to_action.html',
        icon="fa-reply",))
    ,('tab_slider', blocks.ListBlock(
        SliderBlock(),
        template = 'streamfields/tab_slider.html',
        icon="image"))
    ,('actie', blocks.ListBlock(
        ActionBlock(),
        template = 'streamfields/action.html',
        icon="fa-exclamation"))
    ,('logo_blokken', blocks.ListBlock(
        LogoBlock(), 
        template = 'streamfields/logo_block.html', 
        icon="image"))
    ,('download_link', blocks.ListBlock(
        DownloadLinkBlock(),
        template = 'streamfields/download_link.html',
        icon='fa-download'))
    ,('rev_slider', blocks.ListBlock(
        RevSliderBlock(), 
        template = 'streamfields/rev_slider.html', 
        icon="image"))
    ,('medewerker', blocks.ListBlock(
        CoworkerBlock(),
        template = 'streamfields/coworker.html',
        icon="fa-user-plus"))
    ,('project', blocks.ListBlock(
        ProjectBlock(),
        template = 'streamfields/project.html',
        icon="fa-comments-o"))
    ,('google_maps', GoogleMapsBlock(
        template = 'streamfields/google_maps.html',
        icon='fa-map-o'))
    ,]

# Check if oscar_wagtail is in installed apps so they can access product streamfield
if 'oscar_wagtail' in settings.INSTALLED_APPS:
    from oscar.core.loading import get_model
    class ProductChooserBlock(blocks.ChooserBlock):
        @cached_property
        def target_model(self):
            return get_model('catalogue', 'Product')

        widget = forms.Select

        class Meta:
            app_label = 'catalogue'

        def value_for_form(self, value):
            # return the key value for the select field
            if isinstance(value, self.target_model):
                return value.pk
            else:
                return value


    class ProductBlock(blocks.StructBlock):
        products = blocks.ListBlock(ProductChooserBlock)
    
    grid_array.append(
        ('product', blocks.ListBlock(
            ProductBlock(),
            template = 'streamfields/product.html',
            icon="fa-shopping-cart")
        ),
    )

validated_grid_array = []
STREAMFIELDS = settings.STREAMFIELDS
EXCLUDE_STREAMFIELDS = settings.EXCLUDE_STREAMFIELDS

# validate streamfields
if STREAMFIELDS == '__all__':
    if len(EXCLUDE_STREAMFIELDS) > 0:
        for streamfield in grid_array:
            if streamfield[0] not in EXCLUDE_STREAMFIELDS:
                validated_grid_array.append(streamfield)
    else:
        validated_grid_array = grid_array
else:
    for streamfield in grid_array:
        if streamfield[0] in STREAMFIELDS:
            validated_grid_array.append(streamfield)


class GridBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=50,
        required=False,
        classname="grid-title"
    )
    grid = GridChoiceBlock(
        label = 'Breedte kolom',
        help_text = 'De breedte kolommen (*/12).',
    )
    content = blocks.StreamBlock(
        validated_grid_array,
        label="Inhoud"
    )


