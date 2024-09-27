from django import forms

class PersonForm(forms.Form):
    STATUS_CHOICE = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived'),
    )

    person_name = forms.CharField(
        label='',
        initial = 'Nalan',
        widget=forms.TextInput(attrs={'placeholder': 'Search'}),
        max_length=10,
    )
    age = forms.IntegerField()

    # both generate <input type="email"> but only first validates properly
    email_as_field = forms.EmailField()
    email_as_widget = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )


    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICE,
    # )

    # status = forms.IntegerField(
    #     widget=forms.Select(choices=STATUS_CHOICE)
    # )

    # single choice
    status = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=STATUS_CHOICE,
    )

    # multiple choice
    checkboxes = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STATUS_CHOICE
    )
