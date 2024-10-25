class DisableFieldMixin:
    def disable_fields(self):

        if hasattr(self, 'fields'):
            for field_name in self.fields.keys():
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()
