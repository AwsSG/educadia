from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_names', 'last_name', 'user_type', 'bio', 'image']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_names': 'Full name',
            'last_name': 'Last name',
            'user_type': 'User type',
            'bio': 'Short bio/summary',
            'image': 'Upload your image',
        }

        self.fields['bio'].widget = forms.Textarea()
        self.fields['first_names'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control f-input'
            self.fields[field].label = False
