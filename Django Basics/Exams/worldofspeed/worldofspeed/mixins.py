from django import forms

class URLPlaceHolderMixin:
    def add_url_placeholder(self):
        if hasattr(self, 'fields'):
            for field_name, field in self.fields.items():
                if field_name == 'image_url':
                    field.widget = forms.URLInput(attrs={
                        'placeholder': 'https://...',
                    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_url_placeholder()


class ReadOnlyMixin:
    def make_fields_readonly(self):
        readonly_fields = getattr(self, 'readonly_fields', [])

        if hasattr(self, 'fields'):
            for field_name in self.fields.keys():
                if field_name in readonly_fields:
                    self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()
