from django.forms import forms


class DisableFieldsMixin(forms.Form):
    disabled_fields = ()
    readonly_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == '__all__' or field_name in self.disabled_fields:
                field.disabled = True

            if self.readonly_fields[0] == '__all__' or field_name in self.readonly_fields:
                field.widget.attrs['readonly'] = True
