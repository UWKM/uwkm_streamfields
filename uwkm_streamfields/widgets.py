from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class ColorPickerWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        if value is None:
        	value = ''

        colors = settings.CP_COLORS
        
        return rendered + mark_safe(u'''<script type="text/javascript">
            var field = $('#%s');
            field.wrap('<div class="bfh-colorpicker" data-color="%s" data-name="%s" data-colors="%s"></div>');
			$colorpicker = field.parent();
			$colorpicker.bfhcolorpicker($colorpicker.data());
            </script>''' % (name, value, name, ",".join(colors)))
