
class PlaceHolderMixin:
    PLACEHOLDER_OPTIONS = {
        'first_name': 'Enter your first name...',
        'last_name': 'Enter your last name...',
        'passcode': 'Enter 6 digits...',
        'pets_number': 'Enter the number of your pets...',
        'title': 'Put an attractive and unique title...',
        'content': 'Share some interesting facts about your adorable pets...'
    }

    def add_placeholder(self):
        if hasattr(self, 'fields'):
            for field_name, field in self.fields.items():
                if field_name in self.PLACEHOLDER_OPTIONS:
                    field.widget.attrs.update({
                        'placeholder': self.PLACEHOLDER_OPTIONS[field_name],
                    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder()


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
