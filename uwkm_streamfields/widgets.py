from django import forms
from django.utils.safestring import mark_safe

from .models import StreamfieldsSettings as settings

class ColorPickerWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        if value is None:
            value = '#fff'

        return rendered + mark_safe(u'''<script type="text/javascript">
            var field = $('#%s');
            field.ColorPicker();
            field.ColorPickerSetColor('%s');
            </script>''' % (name, value))
