from django import forms
from .models import Donate


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'phone', 'email', 'amount']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name/your organization name',
            'phone': 'Your phone number',
            'email': 'Your email address',
            'amount': '$',
            }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control f-input'
            self.fields[field].label = False
