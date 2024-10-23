from django import forms


class PlaceHolderMixin:
    def add_placeholders(self):
        if hasattr(self, 'fields'):
            for field_name, field in self.fields.items():
                if field_name == 'password':
                    field.widget = forms.PasswordInput(attrs={
                        'placeholder': 'Password',
                    })

                else:
                    placeholder = ' '.join(word.capitalize() for word in field_name.replace('_', ' ').split())
                    field.widget.attrs.update({
                            'placeholder': placeholder,
                    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class LabelRemoveMixin:
    def remove_labels(self):
        if hasattr(self, 'fields'):
            for field_name, field in self.fields.items():
                field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_labels()


class FieldDisableMixin:
    def disable_fields(self):
        if hasattr(self, 'fields'):
            for field_name in self.fields.keys():
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()
