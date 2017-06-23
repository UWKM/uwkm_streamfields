from django import forms
from django.utils.safestring import mark_safe

from .models import StreamfieldsSettings as settings

class ColorPickerWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        if value is None:
            value = ''

        try:
            colors = settings.objects.first().pre_selected_colors.strip().replace('\r', '').replace('\n', '').split(';')
        except:
            colors = ['#000000', '#FFFFFF']
        return rendered + mark_safe(u'''<script type="text/javascript">
            var field = $('#%s');
            field.wrap('<div class="bfh-colorpicker" data-color="%s" data-name="%s" data-colors="%s"></div>');
            $colorpicker = field.parent();
            $colorpicker.bfhcolorpicker($colorpicker.data());
            </script>''' % (name, value, name, ",".join(colors[:7])))
